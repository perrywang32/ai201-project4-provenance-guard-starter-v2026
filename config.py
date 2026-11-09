"""
Settings for Provenance Guard.

Everything you're likely to change lives here, at the top, on purpose.

You'll edit the thresholds in Milestone 5 and the rate limits in unit 8.
"""

import os
from pathlib import Path

ROOT = Path(__file__).parent


# ─── The service ─────────────────────────────────────────────────────────────

# `127.0.0.1` is loopback — only your own machine can reach it, which is what
# you want all through units 7 and 8. A host somewhere else has to accept
# traffic from outside the box, and that means `0.0.0.0`. Setting the env var
# is how you get it; the default keeps your local `curl` commands unchanged.
HOST = os.getenv("HOST", "127.0.0.1")
PORT = int(os.getenv("PORT", "5000"))

# Flask's debug mode gives anyone who can reach the service an interactive
# Python prompt inside your process. Fine on loopback, a gift to strangers
# anywhere else — so it turns itself off the moment HOST isn't loopback.
DEBUG = os.getenv("AI201_DEBUG", "1") == "1" and HOST in ("127.0.0.1", "localhost")


# ─── The local model ─────────────────────────────────────────────────────────
# Your first signal runs a language model ON YOUR OWN MACHINE. No account, no
# key, no card. It downloads about 550 MB the first time — do that before
# class, not during it.
#
# What it measures: how *predictable* your text is to a language model. Text a
# model finds easy to predict tends to be text a model wrote.
#
# The first call is the slow one — ten to twenty seconds while the model loads,
# longer on an older laptop. After that it stays in memory and a submission
# takes a second or two. That cost is part of what you're learning: this is
# what running a model inline in a request actually looks like.

DETECTOR_MODEL = os.getenv("AI201_DETECTOR_MODEL", "gpt2")

# Longer text gives a steadier reading but takes longer. 400 tokens is roughly
# 300 words, which is enough for the signal to mean something.
DETECTOR_MAX_TOKENS = 400


# ─── Scoring (Milestone 4) ───────────────────────────────────────────────────
# How much each signal counts toward the combined score.
#
# ⚠️ These are placeholders. Milestone 4 asks you to write your combining rule
# down BEFORE you code it, and to put the numbers in your README. Whatever you
# decide, it goes here.

WEIGHT_MODEL_SIGNAL = 0.5
WEIGHT_STYLE_SIGNAL = 0.5


# ─── Style signal internals (Milestone 4) ────────────────────────────────────
# How stylometry.style_signal turns its three raw measures into one 0–1 score.
# Every raw measure runs "higher = more human"; each is flipped and mapped onto
# 0–1 with a clamped straight line between two anchors:
#
#   raw value at or past the AI anchor     -> 1.0 (fully AI-ish)
#   raw value at or past the human anchor  -> 0.0 (fully human-ish)
#
# ⚠️ These are starting assumptions, not measured values. Why each was picked:
#   spread  0.20 / 0.65  Coefficient of variation of sentence length. Generated
#                        prose tends toward even mid-length sentences (CV ~0.2);
#                        casual human writing mixes 3-word and 40-word ones.
#   ttr     0.60 / 0.85  Moving-average type-token ratio over STYLE_TTR_WINDOW
#                        words; lower means more repetition. ⚠️ First trial
#                        samples all landed 0.89–0.95 at a 25-word window, i.e.
#                        past the human anchor, so as set this measure adds 0
#                        to every text. Recalibrate against the four inputs.
#   punct   0.06 / 0.20  Punctuation marks per word. ~0.06 is little beyond full
#                        stops; ~0.20 is dense commas, dashes, brackets.
# Record what the four calibration inputs show in the README, then adjust.

STYLE_ANCHORS = {
    "spread": (0.20, 0.65),
    "ttr":    (0.60, 0.85),
    "punct":  (0.06, 0.20),
}

# Spread is the most-cited cue, punctuation the shakiest (some models lean hard
# on em dashes, which pushes it the "human" way). Must sum to 1.0.
STYLE_WEIGHTS = {"spread": 0.5, "ttr": 0.3, "punct": 0.2}

# Type-token ratio falls as text gets longer, so it is always measured over a
# fixed-size sliding window. Text shorter than one window is "too short to
# judge" for that measure (neutral 0.5) — never a different formula.
STYLE_TTR_WINDOW = 25

# Below this many words, punctuation density is too noisy to count (neutral).
STYLE_MIN_WORDS_PUNCT = 20


# ─── Thresholds (Milestone 5) ────────────────────────────────────────────────
# Where one label becomes another. Scores run 0.0 (confidently human) to 1.0
# (confidently AI).
#
#   score < HUMAN_THRESHOLD          -> high-confidence human
#   between the two                  -> unsure
#   score > AI_THRESHOLD             -> high-confidence AI
#
# ⚠️ This is where your false-positive decision from Milestone 1 actually gets
# made. Widening the unsure band means fewer wrong accusations and more AI text
# getting through. There is no setting that avoids the trade — only settings
# that decide who pays for it.

HUMAN_THRESHOLD = 0.35
AI_THRESHOLD = 0.65

# ⚠️ One thing that catches people out in Milestone 5. A weighted average can
# only land between its two inputs — so while `style_signal` is still the stub
# returning 0.5, the combined score can never leave 0.25–0.75 no matter what
# the model signal says, and the human label needs a model score below 0.20 to
# be reachable at all.
#
# If a label you can't reach is the problem, the fix is upstream of the
# thresholds: a style signal that actually varies. `scoring.label_ranges()`
# prints the bands; the reachable range is a different question.


# ─── Rate limiting (UNIT 8) ──────────────────────────────────────────────────
# Off in unit 7. You turn it on and choose the numbers in unit 8, Milestone 1.
#
# Think about two people: a real writer submitting their own work a few times
# an hour, and a script sending a thousand variations to map your thresholds.
# Your README has to say why your numbers and not others.

RATE_LIMITING_ENABLED = os.getenv("AI201_RATE_LIMITS", "0") == "1"

RATE_LIMIT_PER_MINUTE = 10
RATE_LIMIT_PER_DAY = 200

# Flask-Limiter warns loudly without this. In-memory is right for one laptop
# and wrong for anything real — a restart forgets every count, and two copies
# of the service wouldn't share limits.
RATE_LIMIT_STORAGE = "memory://"


# ─── Paths ───────────────────────────────────────────────────────────────────

LOG_DIR = ROOT / "logs"
AUDIT_LOG = LOG_DIR / "audit.jsonl"
RESULTS_DIR = ROOT / "results"
