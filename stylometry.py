"""
Signal two: the style signal. ← YOU BUILD THIS IN MILESTONE 4

Signal one reads the text for meaning. This one measures it *as text* — the
shape of it, without understanding a word.

Three measures are stubbed below because the brief names those three. They are
stubs, not implementations: what they compute is yours, and so is how you
combine them.

    sentence_length_spread   do sentences vary in length, or march in step?
    type_token_ratio         how much of the vocabulary repeats?
    punctuation_density      how much punctuation, and how varied?

Why these might differ between human and AI writing: generated prose tends
toward even, mid-length sentences and a narrower band of vocabulary, because
that's what "most likely next word" produces on average. Human writing is
lumpier — a three-word sentence next to a forty-word one.

⚠️ **The blind spot, which you have to name in Milestone 1.**

This signal cannot read. It has no idea what the text says. Anything that
changes the shape without changing the substance moves it — adding typos,
breaking up sentences, pasting in a quotation. That is a very cheap thing for
someone to do on purpose, and unit 8's attack set will do it to you.

Build each function on its own and call it from a terminal before you wire
anything together:

    python stylometry.py "some text to look at"
"""

import re
import statistics
import string

import config


def sentences(text: str) -> list[str]:
    """Split into sentences. Rough and good enough — given to you."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p.strip()]


def words(text: str) -> list[str]:
    """Split into lowercase words, punctuation stripped. Given to you."""
    return re.findall(r"[a-z0-9']+", text.lower())


# ── The three measures — YOU BUILD THESE ─────────────────────────────────────

def sentence_length_spread(text: str) -> float:
    """
    How much sentence length varies. ← TODO

    Returns:
        A float. Decide yourself what scale it's on and which direction means
        "more human" — then write that down, because your combining rule
        depends on knowing it.

    A hint on what you're reaching for: the standard deviation of sentence
    lengths, probably divided by the mean so a long text and a short one are
    comparable. `statistics.stdev` is imported for you.

    Watch the edge case: a one-sentence submission has no spread at all, and
    `stdev` raises on fewer than two values. Decide what that should return
    before the attack set decides for you.
    """
    # Scale: coefficient of variation (stdev / mean of words-per-sentence).
    # Usually 0.0–1.0, can exceed 1. HIGHER = more varied = more human.
    # Edge case: fewer than two sentences has no measurable spread, so this
    # returns 0.0 — style_signal checks the sentence count and treats that
    # case as "no evidence" rather than reading 0.0 as "very AI".
    lengths = [len(words(s)) for s in sentences(text)]
    lengths = [n for n in lengths if n > 0]
    if len(lengths) < 2:
        return 0.0
    mean = statistics.mean(lengths)
    return statistics.stdev(lengths) / mean


def type_token_ratio(text: str) -> float:
    """
    Unique words over total words. ← TODO

    Returns:
        A float between 0 and 1. Higher means more varied vocabulary.

    Worth knowing before you rely on it: this measure falls as text gets
    longer, because common words repeat. Two texts of different lengths aren't
    directly comparable on it, and if your test inputs vary a lot in length,
    that alone can look like a signal.
    """
    # To blunt the length problem this is a *moving-average* TTR (MATTR):
    # slide a fixed window (config.STYLE_TTR_WINDOW words) across the text,
    # take the TTR of each window, and average them. Every window is the same
    # length, so a long essay and a short paragraph are compared on equal
    # footing. One formula for every text — no fallback.
    # Edge case: text shorter than one window can't be measured, so this
    # returns 0.0 and style_signal treats it as "too short" (neutral), the
    # same way it handles a single sentence.
    # HIGHER = more varied vocabulary = more human.
    window = config.STYLE_TTR_WINDOW
    tokens = words(text)
    if len(tokens) < window:
        return 0.0
    ratios = [
        len(set(tokens[i:i + window])) / window
        for i in range(len(tokens) - window + 1)
    ]
    return statistics.mean(ratios)


# Everything in string.punctuation except the apostrophe (it lives inside
# words like "don't", which words() already keeps), plus typographic dashes,
# ellipsis and curly quotes that string.punctuation doesn't include.
PUNCTUATION = (set(string.punctuation) - {"'"}) | set("—–…“”‘’")


def punctuation_density(text: str) -> float:
    """
    How much punctuation, relative to length. ← TODO

    Returns:
        A float. Whether you count all punctuation or only some kinds — commas,
        semicolons, dashes — is a real choice. Semicolons and em dashes are
        more interesting than full stops, because they vary more between
        writers.
    """
    # Scale: punctuation marks per word, counting all kinds (see PUNCTUATION).
    # Typical prose sits around 0.05–0.25. HIGHER = busier, more irregular
    # punctuation = treated as more human.
    # Caveat: some recent models lean hard on em dashes, which pushes this
    # the "human" way. That's one reason it gets the smallest weight below.
    n_words = len(words(text))
    if n_words == 0:
        return 0.0
    marks = sum(1 for ch in text if ch in PUNCTUATION)
    return marks / n_words


# ── Combining them ───────────────────────────────────────────────────────────

def style_signal(text: str) -> float:
    """
    The style signal as a 0–1 score. **Higher means more likely AI.** ← TODO

    Combine your three measures into one number. Same direction as
    `detector.model_signal`, so that `scoring.combine_signals` can treat them
    the same way — if one of your signals runs backwards, everything above it
    is wrong in a way that's hard to see.

    Two things to decide and write down:

      1. Which direction each measure points. Low spread means more AI-ish, so
         it needs flipping. Work out which of your three need that.
      2. How to get each onto a comparable scale. A raw type-token ratio sits
         between 0 and 1; a raw punctuation count doesn't. Adding them
         unscaled means whichever has the bigger numbers wins by default.

    Test it on the four calibration inputs from Milestone 4 — clearly AI,
    clearly human, plain conventional human writing, lightly-edited AI — before
    you trust it. Plain and ordinary, not formal: formal prose reads as *human*
    to signal one, and it is plain writing that gets accused.
    """
    # 1. Direction: all three raw measures run "higher = more human", so all
    #    three get flipped to "higher = more AI".
    # 2. Scale: each is mapped onto 0–1 with a clamped straight line between
    #    two anchors — the raw value that reads as fully AI-ish (→ 1.0) and the
    #    one that reads as fully human-ish (→ 0.0).
    # 3. Combine: weighted average.
    # 4. Too little text to judge → that measure contributes a neutral 0.5.
    # Anchors, weights and minimums all live in config.py, with the reasoning.
    return round(sum(
        config.STYLE_WEIGHTS[k] * v for k, v in style_parts(text).items()
    ), 4)


def style_parts(text: str) -> dict[str, float]:
    """Each measure's 0–1 AI-ness (0.5 = too short to judge). For debugging."""
    anchors = config.STYLE_ANCHORS
    n_words = len(words(text))
    return {
        "spread": (
            _ai_ness(sentence_length_spread(text), *anchors["spread"])
            if len(sentences(text)) >= 2 else 0.5
        ),
        "ttr": (
            _ai_ness(type_token_ratio(text), *anchors["ttr"])
            if n_words >= config.STYLE_TTR_WINDOW else 0.5
        ),
        "punct": (
            _ai_ness(punctuation_density(text), *anchors["punct"])
            if n_words >= config.STYLE_MIN_WORDS_PUNCT else 0.5
        ),
    }


def _ai_ness(value: float, ai_anchor: float, human_anchor: float) -> float:
    """Map a raw 'higher = more human' measure onto 0–1, higher = more AI."""
    t = (value - ai_anchor) / (human_anchor - ai_anchor)
    return 1.0 - max(0.0, min(1.0, t))


if __name__ == "__main__":
    import sys

    text = " ".join(sys.argv[1:]) or (
        "The system works well. It handles most cases correctly and provides "
        "good results. Users generally find it easy to use and understand."
    )

    print(f"{len(sentences(text))} sentences, {len(words(text))} words\n")
    print(f"sentence_length_spread   {sentence_length_spread(text)}")
    print(f"type_token_ratio         {type_token_ratio(text)}")
    print(f"punctuation_density      {punctuation_density(text)}")
    print(f"\nper-measure AI-ness       {style_parts(text)}   (0.5 = too short)")
    print(f"style_signal             {style_signal(text)}   (higher = more likely AI)")
