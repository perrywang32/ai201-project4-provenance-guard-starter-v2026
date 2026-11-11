# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->

1. A writer's client sends JSON containing `text` and `creator_id` to `POST /submit`.
2. `app.py` validates the request, required fields, and text length. Invalid requests receive an error response.
3. `detector.model_signal(text)` uses GPT-2 perplexity to produce `model_score`; higher means more likely AI.
4. `stylometry.style_signal(text)` measures sentence-length spread, vocabulary variety, and punctuation to produce `style_score`.
5. `scoring.combine_signals(model_score, style_score)` takes their equal-weight average as `combined_score`.
6. `scoring.score_to_label(combined_score)` maps the result to a human, unsure, or AI label. The response includes the scores, guess, confidence, label, and `content_id`.
7. `audit.log_decision(...)` records the decision in `logs/audit.jsonl`. `GET /log` returns recent records. A writer can send `POST /appeal` with a `content_id` and reasoning; a valid appeal is added to the log and changes the status to `under_review` while the original decision remains recorded.

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:** GPT-2 perplexity: how predictable or surprising the next words in the text are to the model. detector.py maps that value to a 0–1 model score, where higher means more likely AI.

**Why that might differ between human and AI writing:** AI-generated text may follow patterns that a language model finds predictable. Human writing can use less predictable wording or sentence choices. This is only a heuristic; the scores can overlap.

**What it can't see:** It cannot verify who wrote the text or understand the writer's intent. Predictable human writing can look AI-like, and edited or unusual AI writing can look more human. Topic and writing style can also affect predictability.
### Signal two — the style signal

**What it measures:** Sentence-length spread (coefficient of variation), moving-average type-token ratio over 25-word windows, and punctuation marks per word.

**Why that might differ between human and AI writing:** The heuristic assumes generated prose tends to use more even sentence lengths and a narrower vocabulary, while human writing may vary more. These are tendencies, not reliable authorship rules.

**What it can't see:** It does not understand the text or know who wrote it. Editing sentence breaks, adding quotations, or changing punctuation can change its score without changing the meaning.

**Observed limitation:** In my four calibration samples, the TTR component scored 0.0 for all four because each raw value exceeded the 0.85 human anchor. The casual human sample scored above both AI samples; the plain-human and lightly-edited-AI scores were nearly tied (0.6603 versus 0.6604). The style signal did not meaningfully separate this small test set in the intended direction.

### The combining rule

**The rule:** I use an equal weighted average of the model and style scores. When they disagree, the combined score falls between them, treating disagreement as uncertainty.

**The numbers:** Model weight = 0.50; style weight = 0.50. Inside the style signal, sentence spread = 0.50, TTR = 0.30, and punctuation = 0.20. The style anchors are in config.py.

**Where it lives:** scoring.py::combine_signals

**A case where my two signals split, and what my rule does with it:** For the casual human sample, the model score was 0.466 and the style score was 0.6817. The equal average produced 0.57385, between the two signal scores. The style signal leaned AI on this human-written sample, which is a limitation I need to keep in mind.

---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.00 - 0.35  | This writing appears more likely to have been written by a person. This result is an estimate, not proof of authorship.  |
| unsure | 0.35 < score < 0.65 | We couldn't confidently determine whether this writing was written by a person or generated by AI. |
| high-confidence AI | 0.65 - 1.00 | This writing appears more likely to have been generated by AI. This result is an estimate, not proof of authorship.  |

**Why I worded the "unsure" one this way:**
<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->
It says plainly that the system could not decide, without accusing the writer or presenting a score as proof. The human and AI labels also call the result an estimate, because these signals cannot establish who authored a text.



---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

These three submissions are the Milestone 3 baseline, from before the second signal was connected. They used creator_id = test-user; model_score was populated, while style_score and combined_score were still placeholders.

**Submission 1 — balanced test sample**

```powershell
$body = '{"text":"Keaton Wagler is a young basketball guard. He is developing his skills and adjusting to the professional game. Consistency and decision making will help shape his role over time.","creator_id":"test-user"}'
Invoke-RestMethod -Uri "http://127.0.0.1:5000/submit" -Method Post -ContentType "application/json" -Body $body
```

```json
{
  "content_id": "57b29c03c6fe474d9dadc97942cdec39",
  "guess": null,
  "confidence": null,
  "label": null,
  "model_score": 0.5176,
  "style_score": null
}
```

**Submission 2 — AI-style sample**

```powershell
$body = '{"text":"Keaton Wagler is a young basketball guard whose game combines scoring, playmaking, and effort on both ends of the court. After playing at Illinois, he now has the opportunity to adjust to the pace and physicality of the NBA with the Los Angeles Clippers. His development will depend on consistency, decision-making, and how well he contributes within the team system. As his career continues, his performances will show how his skills translate to the professional level.","creator_id":"test-user"}'
Invoke-RestMethod -Uri "http://127.0.0.1:5000/submit" -Method Post -ContentType "application/json" -Body $body
```

```json
{
  "content_id": "bfab2728223545cb9936a87a6f9d38d6",
  "guess": null,
  "confidence": null,
  "label": null,
  "model_score": 0.8095,
  "style_score": null
}
```

**Submission 3 — human-written sample**

```powershell
$body = '{"text":"Keaton Wagler is our fifth pick that''s trying to earn a spot on our team. He has shown promising flashes so far and still needs to build up his frame to get better. Our head coach is kinda dumb for not prioritizing playing him to develop his skills and talent as he''s still currently inexperienced professionally.","creator_id":"test-user"}'
Invoke-RestMethod -Uri "http://127.0.0.1:5000/submit" -Method Post -ContentType "application/json" -Body $body
```

```json
{
  "content_id": "0ff1890deefe49ecb0828c7815500ab1",
  "guess": null,
  "confidence": null,
  "label": null,
  "model_score": 0.466,
  "style_score": null
}
```

**What the log shows afterwards**

These are the three entries from `logs/audit.jsonl` (also returned by `GET /log?limit=3`):

```json
{
  "count": 3,
  "entries": [
    {
      "timestamp": "2026-11-09T05:36:08+00:00",
      "content_id": "57b29c03c6fe474d9dadc97942cdec39",
      "creator_id": "test-user",
      "guess": null,
      "model_score": 0.5176,
      "style_score": null,
      "combined_score": null,
      "label": null,
      "status": "decided"
    },
    {
      "timestamp": "2026-11-09T05:39:16+00:00",
      "content_id": "bfab2728223545cb9936a87a6f9d38d6",
      "creator_id": "test-user",
      "guess": null,
      "model_score": 0.8095,
      "style_score": null,
      "combined_score": null,
      "label": null,
      "status": "decided"
    },
    {
      "timestamp": "2026-11-09T05:40:05+00:00",
      "content_id": "0ff1890deefe49ecb0828c7815500ab1",
      "creator_id": "test-user",
      "guess": null,
      "model_score": 0.466,
      "style_score": null,
      "combined_score": null,
      "label": null,
      "status": "decided"
    }
  ]
}
```

**Milestone 4 calibration results**

These are the four actual POST /submit responses after both signals were connected. The labels and confidence are still placeholders for Milestone 5.

| Sample | content_id | model_score | style_score | combined_score |
|---|---|---:|---:|---:|
| Clearly AI | 526874a4113e4baeb427e6f306b93a2e | 0.8239 | 0.6244 | 0.72415 |
| Human, casual | 8a4f5bc3a8df4d83975e3c1de1bec63e | 0.466 | 0.6817 | 0.57385 |
| Lightly edited AI | 5e064d8845ff4047ae70e49716c7b2b0 | 0.7802 | 0.6604 | 0.7203 |
| Plain conventional human | c06a5bfaa03845d981ce361c1ce30636 | 0.6122 | 0.6603 | 0.63625 |

The combined score put the clearly AI sample above the casual human sample. The plain conventional human sample scored closer to the AI examples, so it is an important edge case.

The audit-log block above is the earlier Milestone 3 log. After Milestone 4, run GET /log?limit=4 and replace or supplement that block with the four newest entries showing model_score, style_score, and combined_score.

**Milestone 4 audit log**

This is the actual response from GET /log?limit=4 after the four calibration submissions:

    {
      "count": 4,
      "entries": [
        {
          "combined_score": 0.72415,
          "content_id": "526874a4113e4baeb427e6f306b93a2e",
          "creator_id": "test-user",
          "guess": null,
          "label": null,
          "model_score": 0.8239,
          "status": "decided",
          "style_score": 0.6244,
          "timestamp": "2026-11-09T07:18:56+00:00"
        },
        {
          "combined_score": 0.57385,
          "content_id": "8a4f5bc3a8df4d83975e3c1de1bec63e",
          "creator_id": "test-user",
          "guess": null,
          "label": null,
          "model_score": 0.466,
          "status": "decided",
          "style_score": 0.6817,
          "timestamp": "2026-11-09T07:18:56+00:00"
        },
        {
          "combined_score": 0.72029999999999999,
          "content_id": "5e064d8845ff4047ae70e49716c7b2b0",
          "creator_id": "test-user",
          "guess": null,
          "label": null,
          "model_score": 0.7802,
          "status": "decided",
          "style_score": 0.6604,
          "timestamp": "2026-11-09T07:18:57+00:00"
        },
        {
          "combined_score": 0.63625,
          "content_id": "c06a5bfaa03845d981ce361c1ce30636",
          "creator_id": "test-user",
          "guess": null,
          "label": null,
          "model_score": 0.6122,
          "status": "decided",
          "style_score": 0.6603,
          "timestamp": "2026-11-09T07:18:57+00:00"
        }
      ]
    }

**Clearly AI**

    $body = @{ text = "Keaton Wagler is a promising young basketball player whose development will depend on his ability to adapt to the demands of the professional game. His combination of scoring, playmaking, and effort on both ends of the court gives him several ways to contribute. As he gains experience, consistency and decision-making will be important factors in determining his role with the team."; creator_id = "test-user" } | ConvertTo-Json -Compress
    Invoke-RestMethod -Uri "http://127.0.0.1:5000/submit" -Method Post -ContentType "application/json" -Body $body

    {
      "combined_score": 0.72415,
      "confidence": null,
      "content_id": "526874a4113e4baeb427e6f306b93a2e",
      "guess": null,
      "label": null,
      "model_score": 0.8239,
      "style_score": 0.6244
    }

**Human, casual**

    $body = @{ text = "Keaton Wagler is our fifth pick that's trying to earn a spot on our team. He has shown promising flashes so far and still needs to build up his frame to get better. Our head coach is kinda dumb for not prioritizing playing him to develop his skills and talent as he's still currently inexperienced professionally."; creator_id = "test-user" } | ConvertTo-Json -Compress
    Invoke-RestMethod -Uri "http://127.0.0.1:5000/submit" -Method Post -ContentType "application/json" -Body $body

    {
      "combined_score": 0.57385,
      "confidence": null,
      "content_id": "8a4f5bc3a8df4d83975e3c1de1bec63e",
      "guess": null,
      "label": null,
      "model_score": 0.466,
      "style_score": 0.6817
    }

**Lightly edited AI**

    $body = @{ text = "Keaton Wagler is a promising young player who still has room to grow as he adjusts to the professional game. He can contribute in different ways, but his consistency and decision-making will affect the role he earns. It'll be interesting to see how he develops with more experience as he has shown flashes in limited opportunities."; creator_id = "test-user" } | ConvertTo-Json -Compress
    Invoke-RestMethod -Uri "http://127.0.0.1:5000/submit" -Method Post -ContentType "application/json" -Body $body

    {
      "combined_score": 0.7203,
      "confidence": null,
      "content_id": "5e064d8845ff4047ae70e49716c7b2b0",
      "guess": null,
      "label": null,
      "model_score": 0.7802,
      "style_score": 0.6604
    }

**Plain conventional human**

    $body = @{ text = "Keaton Wagler is the fifth pick for the Clippers that's trying to earn more playing time on the team. He has shown promising flashes that showed why he was such a highly touted pick. He should continue to get only better as the season goes along."; creator_id = "test-user" } | ConvertTo-Json -Compress
    Invoke-RestMethod -Uri "http://127.0.0.1:5000/submit" -Method Post -ContentType "application/json" -Body $body

    {
      "combined_score": 0.63625,
      "confidence": null,
      "content_id": "c06a5bfaa03845d981ce361c1ce30636",
      "guess": null,
      "label": null,
      "model_score": 0.6122,
      "style_score": 0.6603
    }

**Milestone 5 — final label results**

After rewriting the plain conventional human sample, I submitted the four calibration samples again. The latest four entries in `GET /log?limit=10` are timestamped `2026-11-09T10:18:05+00:00`.

| Sample | Model score | Style score | Combined score / confidence | Guess |
|---|---:|---:|---:|---|
| Clearly AI | 0.8239 | 0.6244 | 0.72415 | `ai` |
| Human, casual | 0.466 | 0.6817 | 0.57385 | `unsure` |
| Lightly edited AI | 0.7802 | 0.6604 | 0.7203 | `ai` |
| Plain conventional human, rewritten | 0.4938 | 0.1693 | 0.33155 | `human` |

The first three label outcomes and the rewritten human outcome show that all three label variants are reachable. An earlier version of the conventional-human sample scored `0.36455` and was labeled `unsure`; after rewriting it, the score was `0.33155` and the label was `human`. The log also contains older submissions, which is why its total count is 10.

**Appeal request**

```powershell
$body = @{ content_id = "8a4f5bc3a8df4d83975e3c1de1bec63e"; reasoning = "I wrote this sample myself. The result seems to misread my informal wording." } | ConvertTo-Json -Compress
Invoke-RestMethod -Uri "http://127.0.0.1:5000/appeal" -Method Post -ContentType "application/json" -Body $body
```
**Appeal response**

```text
content_id: 8a4f5bc3a8df4d83975e3c1de1bec63e
message: Thanks, your appeal has been received. A person will review this result. The original decision stays on record until then.
status: under_review
```

**Appeal log entry**

The `GET /log?limit=10` output included this appeal event:

```json
{
  "content_id": "8a4f5bc3a8df4d83975e3c1de1bec63e",
  "creator_id": "test-user",
  "event": "appeal",
  "reasoning": "I wrote this sample myself. The result seems to misread my informal wording.",
  "status": "under_review",
  "timestamp": "2026-11-09T08:03:58+00:00"
}
```

## How I Used AI

**Moment 1 — designing the style signal**

- *What I asked for:* Help understanding what to implement in `style_signal`, how to combine the three measurements, and how to test the result against the calibration examples.
- *What came back:* An explanation of sentence-length spread, type-token ratio, and punctuation density, plus guidance to put them on a comparable 0–1 scale and make higher scores consistently mean more AI-like.
- *What I changed:* I implemented and tuned the function in `stylometry.py`, tested all four samples, and recorded the limitation that the TTR component scored 0.0 for all four because their raw values were above the configured anchor.

**Moment 2 — connecting labels and appeals**

- *What I asked for:* Help understanding how to return reader-facing labels from `/submit`, write the three label variants, and test an appeal through the API.
- *What came back:* Example wording and a step-by-step explanation of how the combined score maps to a label, how `/appeal` uses a `content_id`, and how to verify the status in `GET /log`.
- *What I changed:* I implemented the label mapping and appeal flow, chose the final wording and score ranges, rewrote the plain conventional human sample, and ran the submissions and appeal myself. The results and appeal response above are the outputs I recorded.

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** 10 per minute, 200 per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->
These limits leave room for normal writing and testing while slowing down scripts that send many submissions quickly. In my 15-request flood test, the first 10 requests succeeded and the next 5 were rate-limited.

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->
Requests are counted by `creator_id`. The flood test sent all 15 requests as `flood_tester`, so they shared the same limit.

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```text
200 200 200 200 200 200 200 200 200 200 429 429 429 429 429

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->
I ran `python run_attacks.py --set .\attack_set\attack_set --label before`. The set returned 56 outcomes: **26 BROKE and 30 HELD**. I marked an evasion BROKE when AI text avoided an AI label, and marked a false positive BROKE when human text was labeled AI. I judged prompt-injection rows by whether the instruction changed the service output or log, malformed rows by whether the invalid input was rejected, and flood rows by whether each request was accepted or rate-limited.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---:|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `3521803305a54427b8c01e24d1c7126c` | unsure | 0.382 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `9b47867a16914009a515fa6f70dae820` | human | 0.307 | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `1508ec7058404d4d9d57465c2df1e137` | unsure | 0.469 | BROKE |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `303f4ba2b6894c16996955e02109b92f` | unsure | 0.599 | BROKE |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `9c84c5d75161451cb04e850768e01ed2` | human | 0.181 | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `29f6bb937fe64e80bf5654f5b5317819` | unsure | 0.367 | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | `29007a67a4ad46f38f142eba2b9b8a5f` | unsure | 0.418 | BROKE |
| EV08 | evasion | signal one: text below the token window | 200 | `776e56ca0bfa4681985a10c527d1570d` | unsure | 0.452 | BROKE |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `daa1b35ffc1e401ea9ae942e77beed91` | unsure | 0.500 | BROKE |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `a8c82ab45bdc4c9ea0e79bc83ee429e0` | ai | 0.732 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `7a55cddac788427280584c3056182dbe` | unsure | 0.489 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `09ac83a94c0c4738b08b7cecff528a93` | ai | 0.665 | BROKE |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `5603827d166544e9a88c3d6cd91cfdff` | ai | 0.664 | BROKE |
| FP04 | false_positive | a student essay written to a rubric | 200 | `0e756021dff8495d90136c9b9f09a0d1` | unsure | 0.622 | HELD |
| FP05 | false_positive | technical documentation written by a person | 200 | `008f04a0462c4a97a287522a8d1c002c` | ai | 0.734 | BROKE |
| FP06 | false_positive | a person imitating a formal template | 200 | `d7310065f4384741b17f49e64d86d878` | unsure | 0.584 | HELD |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `3d87eedc13214bc1af065f8ea5810e72` | unsure | 0.543 | HELD |
| FP08 | false_positive | very short genuine human submission | 200 | `03ebcda3a95246baabecc3f5d8f5f589` | unsure | 0.407 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `932493535e404dffa53f30ac3ae248fd` | human | 0.295 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `0b8caddd721c45d89c1773f73b54f453` | human | 0.102 | BROKE |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `1a318136a9d143eebb3995fddf835546` | unsure | 0.520 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `874332958fd44b7f94ce22a768773655` | unsure | 0.391 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `1e8ae23cca094797920f1bcce5e0ec00` | unsure | 0.419 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `a5451b6f1d40464db9c716549d11e4ea` | unsure | 0.466 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 400 | `—` | — | — | HELD |
| MF03 | malformed | text is control characters | 200 | `5caf18267a9b4d35bedc297a6669f969` | human | 0.250 | BROKE |
| MF04 | malformed | text is only punctuation | 200 | `1d6a566ba355499c94c571c89e429048` | unsure | 0.381 | BROKE |
| MF05 | malformed | text is a very long single word | 400 | `—` | — | — | HELD |
| MF06 | malformed | text is emoji only | 400 | `—` | — | — | HELD |
| MF07 | malformed | text is right-to-left script | 200 | `777a7c02ff1a4e3498b050b1c67c39b1` | ai | 0.703 | BROKE |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — | HELD |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | HELD |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — | HELD |
| RQ03 | malformed | text is a number | 400 | `—` | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | `—` | — | — | HELD |
| RQ05 | malformed | text is null | 400 | `—` | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — | HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | `—` | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `e1a06d0efe094652ab0f9ff44fab6a24` | human | 0.264 | BROKE |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `bfa149a4080646b895ff037ae000b133` | human | 0.264 | BROKE |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `bbaf3fd978ef44d1b944eb8511d195a7` | human | 0.264 | BROKE |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `fe5adafc85a344da873c865cff4002ca` | human | 0.264 | BROKE |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `44d9295866ec4a739a70d695233ba6ae` | human | 0.264 | BROKE |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `a2267cdc88584942b9ab6e97328bc098` | human | 0.264 | BROKE |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `d6620bc61a0e48bc9588399c2963a33e` | human | 0.264 | BROKE |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `b5e8f17c673b4740a620fb6f75135447` | human | 0.264 | BROKE |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `8f6494ca7e54446580affb1522fea346` | human | 0.264 | BROKE |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c1e5f08c1c6b4d61978ad1b09ccf05eb` | human | 0.264 | BROKE |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

These entries show PI05 remaining an ordinary decision record and the flood run reaching the configured limit. The flood decisions are repetitive; the two rejection records show where the limiter stopped further submissions.

```json
[
  {
    "content_id": "1e8ae23cca094797920f1bcce5e0ec00",
    "creator_id": "attacker_PI05",
    "guess": "unsure",
    "combined_score": 0.41925,
    "model_score": 0.6401,
    "style_score": 0.1984,
    "label": "We couldn't confidently determine whether this writing was written by a person or generated by AI.",
    "status": "decided",
    "timestamp": "2026-11-10T10:10:55+00:00"
  },
  {
    "combined_score": 0.26435,
    "content_id": "e1a06d0efe094652ab0f9ff44fab6a24",
    "creator_id": "attacker_flood",
    "guess": "human",
    "label": "This writing appears more likely to have been written by a person. This result is an estimate, not proof of authorship.",
    "model_score": 0.0287,
    "status": "decided",
    "style_score": 0.5,
    "timestamp": "2026-11-10T10:10:56+00:00"
  },
  {
    "combined_score": 0.26435,
    "content_id": "bfa149a4080646b895ff037ae000b133",
    "creator_id": "attacker_flood",
    "guess": "human",
    "label": "This writing appears more likely to have been written by a person. This result is an estimate, not proof of authorship.",
    "model_score": 0.0287,
    "status": "decided",
    "style_score": 0.5,
    "timestamp": "2026-11-10T10:10:56+00:00"
  },
  {
    "combined_score": 0.26435,
    "content_id": "bbaf3fd978ef44d1b944eb8511d195a7",
    "creator_id": "attacker_flood",
    "guess": "human",
    "label": "This writing appears more likely to have been written by a person. This result is an estimate, not proof of authorship.",
    "model_score": 0.0287,
    "status": "decided",
    "style_score": 0.5,
    "timestamp": "2026-11-10T10:10:56+00:00"
  },
  {
    "combined_score": 0.26435,
    "content_id": "fe5adafc85a344da873c865cff4002ca",
    "creator_id": "attacker_flood",
    "guess": "human",
    "label": "This writing appears more likely to have been written by a person. This result is an estimate, not proof of authorship.",
    "model_score": 0.0287,
    "status": "decided",
    "style_score": 0.5,
    "timestamp": "2026-11-10T10:10:56+00:00"
  },
  {
    "combined_score": 0.26435,
    "content_id": "44d9295866ec4a739a70d695233ba6ae",
    "creator_id": "attacker_flood",
    "guess": "human",
    "label": "This writing appears more likely to have been written by a person. This result is an estimate, not proof of authorship.",
    "model_score": 0.0287,
    "status": "decided",
    "style_score": 0.5,
    "timestamp": "2026-11-10T10:10:56+00:00"
  },
  {
    "combined_score": 0.26435,
    "content_id": "a2267cdc88584942b9ab6e97328bc098",
    "creator_id": "attacker_flood",
    "guess": "human",
    "label": "This writing appears more likely to have been written by a person. This result is an estimate, not proof of authorship.",
    "model_score": 0.0287,
    "status": "decided",
    "style_score": 0.5,
    "timestamp": "2026-11-10T10:10:56+00:00"
  },
  {
    "combined_score": 0.26435,
    "content_id": "d6620bc61a0e48bc9588399c2963a33e",
    "creator_id": "attacker_flood",
    "guess": "human",
    "label": "This writing appears more likely to have been written by a person. This result is an estimate, not proof of authorship.",
    "model_score": 0.0287,
    "status": "decided",
    "style_score": 0.5,
    "timestamp": "2026-11-10T10:10:56+00:00"
  },
  {
    "creator_id": "attacker_flood",
    "event": "rejected",
    "limit": "10 per 1 minute",
    "reason": "rate_limited",
    "status": "rejected",
    "timestamp": "2026-11-10T10:10:56+00:00"
  },
  {
    "creator_id": "attacker_flood",
    "event": "rejected",
    "limit": "10 per 1 minute",
    "reason": "rate_limited",
    "status": "rejected",
    "timestamp": "2026-11-10T10:10:56+00:00"
  }
]
```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:

FP05, technical documentation written by a person, was labeled `ai` with a combined score of **0.734**. A false AI accusation against someone’s professional writing could harm their credibility, even though the label says the result is only an estimate.


---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. False positives | At most 1 of 10 known human samples labeled AI in each trial | 2/10 labeled AI | 2/10 labeled AI | 2/10 labeled AI | MISSED |
| 2. Score spread | Mean AI score at least 0.15 above mean human score | AI 0.48119; human 0.50578; difference -0.02459 | AI 0.48119; human 0.50578; difference -0.02459 | AI 0.48119; human 0.50578; difference -0.02459 | MISSED |
| 3. Label coverage | Each trial includes human, unsure, and AI | unsure, unsure, AI; no human | unsure, unsure, AI; no human | unsure, unsure, AI; no human | MISSED |
| 4. Appeals | Valid appeal moves status to `under_review` and adds a log entry | MET in one earlier manual appeal | Not run | Not run | INCOMPLETE — 1 of 3 |
| 5. Bad input | Missing, empty, and over-400-token text each return 400 with an error message and no server error | 400, 400, 400 | 400, 400, 400 | 400, 400, 400 | MET for status/no server error; error text not captured in this report |


**Real output from one trial**, copied from `results/run_2026-11-10_2102_before.md`. The report was produced by `run_eval.py::main`; `/submit` is `app.py::submit`.

### Criterion 1 — false positives, Trial 1

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.57385,
    "model_score": 0.466,
    "style_score": 0.6817,
    "label": "We couldn't confidently determine whether this writing was written by a person or generated by AI.",
    "sent": "Keaton Wagler is our fifth pick that's trying to earn a spot on our te"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.33555,
    "model_score": 0.5018,
    "style_score": 0.1693,
    "label": "This writing appears more likely to have been written by a person. This result is an estimate, not proof of authorship.",
    "sent": "Keaton Wagler is the fifth pick for the Clippers that's trying to earn"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3524,
    "model_score": 0.4631,
    "style_score": 0.2417,
    "label": "We couldn't confidently determine whether this writing was written by a person or generated by AI.",
    "sent": "Ty Lue hasn't been great at developing talent lately, he has been prio"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7799,
    "model_score": 0.8377,
    "style_score": 0.7221,
    "label": "This writing appears more likely to have been generated by AI. This result is an estimate, not proof of authorship.",
    "sent": "The Clippers have a lot of young talent that needs to be developed, bu"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.48719999999999997,
    "model_score": 0.5244,
    "style_score": 0.45,
    "label": "We couldn't confidently determine whether this writing was written by a person or generated by AI.",
    "sent": "This team is leading the league in turnovers per game, yet the coachin"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.33545,
    "model_score": 0.2304,
    "style_score": 0.4405,
    "label": "This writing appears more likely to have been written by a person. This result is an estimate, not proof of authorship.",
    "sent": "Baba Miller alongside Keaton Wagler have been making a very positive i"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.69495,
    "model_score": 0.846,
    "style_score": 0.5439,
    "label": "This writing appears more likely to have been generated by AI. This result is an estimate, not proof of authorship.",
    "sent": "The Los Angeles Rams have a glaring need at wide receiver due to injur"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.58385,
    "model_score": 0.6119,
    "style_score": 0.5558,
    "label": "We couldn't confidently determine whether this writing was written by a person or generated by AI.",
    "sent": "The Dodgers are looking to re-sign Tarik Skubal but they might get int"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5337000000000001,
    "model_score": 0.4011,
    "style_score": 0.6663,
    "label": "We couldn't confidently determine whether this writing was written by a person or generated by AI.",
    "sent": "Mercedes C300 is a great car, but the family BMW 530 series is a whole"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.48905,
    "model_score": 0.2781,
    "style_score": 0.7,
    "label": "We couldn't confidently determine whether this writing was written by a person or generated by AI.",
    "sent": "Kawhi Leonard is kinda hated in Clippernation due to the Aspirations s"
  }
]
```

### Criterion 2 — score spread, Trial 1

The first five entries are the AI-generated group; the next five are the human-written group.

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5756,
    "model_score": 0.4726,
    "style_score": 0.6786,
    "label": "We couldn't confidently determine whether this writing was written by a person or generated by AI.",
    "sent": "Keaton Wagler's development will depend on how quickly he adjusts to t"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4476,
    "model_score": 0.3605,
    "style_score": 0.5347,
    "label": "We couldn't confidently determine whether this writing was written by a person or generated by AI.",
    "sent": "A young guard can influence a game without leading the team in scoring"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.33385,
    "model_score": 0.4693,
    "style_score": 0.1984,
    "label": "This writing appears more likely to have been written by a person. This result is an estimate, not proof of authorship.",
    "sent": "The coaching staff will likely evaluate Wagler across several areas, i"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.48365,
    "model_score": 0.4772,
    "style_score": 0.4901,
    "label": "We couldn't confidently determine whether this writing was written by a person or generated by AI.",
    "sent": "Wagler has potential, but potential alone does not guarantee a permane"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.56525,
    "model_score": 0.4672,
    "style_score": 0.6633,
    "label": "We couldn't confidently determine whether this writing was written by a person or generated by AI.",
    "sent": "The most useful measure of Wagler's progress may be whether he becomes"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.57385,
    "model_score": 0.466,
    "style_score": 0.6817,
    "label": "We couldn't confidently determine whether this writing was written by a person or generated by AI.",
    "sent": "Keaton Wagler is our fifth pick that's trying to earn a spot on our te"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.33555,
    "model_score": 0.5018,
    "style_score": 0.1693,
    "label": "This writing appears more likely to have been written by a person. This result is an estimate, not proof of authorship.",
    "sent": "Keaton Wagler is the fifth pick for the Clippers that's trying to earn"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3524,
    "model_score": 0.4631,
    "style_score": 0.2417,
    "label": "We couldn't confidently determine whether this writing was written by a person or generated by AI.",
    "sent": "Ty Lue hasn't been great at developing talent lately, he has been prio"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7799,
    "model_score": 0.8377,
    "style_score": 0.7221,
    "label": "This writing appears more likely to have been generated by AI. This result is an estimate, not proof of authorship.",
    "sent": "The Clippers have a lot of young talent that needs to be developed, bu"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.48719999999999997,
    "model_score": 0.5244,
    "style_score": 0.45,
    "label": "We couldn't confidently determine whether this writing was written by a person or generated by AI.",
    "sent": "This team is leading the league in turnovers per game, yet the coachin"
  }
]
```

### Criterion 3 — label coverage, Trial 1

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5756,
    "model_score": 0.4726,
    "style_score": 0.6786,
    "label": "We couldn't confidently determine whether this writing was written by a person or generated by AI.",
    "sent": "Keaton Wagler's development will depend on how quickly he adjusts to t"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.57385,
    "model_score": 0.466,
    "style_score": 0.6817,
    "label": "We couldn't confidently determine whether this writing was written by a person or generated by AI.",
    "sent": "Keaton Wagler is our fifth pick that's trying to earn a spot on our te"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.6778500000000001,
    "model_score": 0.7204,
    "style_score": 0.6353,
    "label": "This writing appears more likely to have been generated by AI. This result is an estimate, not proof of authorship.",
    "sent": "Keaton Wagler is a promising young player who still has room to grow a"
  }
]
```

### Criterion 4 — appeals, three manual trials

Each valid appeal returned `under_review`, and each appears in the audit log as an `appeal` event.

**Trial 1 — earlier appeal**

```json
{
  "content_id": "8a4f5bc3a8df4d83975e3c1de1bec63e",
  "creator_id": "test-user",
  "event": "appeal",
  "reasoning": "I wrote this sample myself. The result seems to misread my informal wording.",
  "status": "under_review",
  "timestamp": "2026-11-09T08:03:58+00:00"
}
```

**Trial 2 — fresh submission appeal**

```json
{
  "content_id": "7e2e639d2e064a7cbd8d265e9dd9b54f",
  "creator_id": "test-user",
  "event": "appeal",
  "reasoning": "I wrote this sample myself; I am testing the appeal workflow.",
  "status": "under_review",
  "timestamp": "2026-11-11T05:18:21+00:00"
}
```

**Trial 3 — fresh submission appeal**

```json
{
  "content_id": "d52310e5ab004870b88d39c040e160f2",
  "creator_id": "test-user",
  "event": "appeal",
  "reasoning": "I wrote this sample myself; I am testing the appeal workflow.",
  "status": "under_review",
  "timestamp": "2026-11-11T05:23:52+00:00"
}
```

### Criterion 5 — bad input, Trial 1

```json
[
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"creator_id\": \"eval_missing_text\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "(empty text)"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "word word word word word word word word word word word word word word "
  }
]
```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->
### Missed criteria

- **Criterion 1 — MISSED:** Two of ten human samples were labeled AI in every trial. The Clippers paragraph scored 0.7799 combined (model 0.8377, style 0.7221); the Rams paragraph scored 0.69495 (model 0.846, style 0.5439). Both signals scored these human samples as AI-like, and the combined score crossed the AI-label threshold.

- **Criterion 2 — MISSED:** The AI samples averaged 0.48119, while the human samples averaged 0.50578. Their scores overlapped: one AI sample scored 0.33385, while one human sample scored 0.7799. The model and style signals did not separate these samples enough for the combined score to meet my target.

- **Criterion 3 — MISSED:** All three trials returned `unsure, unsure, ai`; none returned `human`. My human sample scored 0.57385 and mapped to `unsure`, so these inputs did not reach the human-label range.

### Broken attacks

- **EV01, EV02, EV03, EV06, EV07, EV09 — BROKE:** These AI evasion inputs returned `unsure` or `human`. Their typos, altered sentence lengths, quotation, punctuation, or human-written opening affected the signals’ measurements and pulled the combined score out of the AI-label range.

- **EV04 — BROKE:** Unusual wording raised the model score to 0.6114, but the combined score was 0.5989 and the label stayed `unsure`. The combining and label-mapping stages did not produce an AI label.

- **EV05 — BROKE:** The heavy editing pass scored low on both signals (model 0.3212, style 0.0418), resulting in a human label. Both signals read the edited AI text as human-like.

- **EV08 — BROKE:** Text below the model’s token window received a low model score (0.2452); the combined score was 0.4516 and the result was `unsure`. The model signal did not identify the short AI text.

- **FP02, FP03, FP05 — BROKE:** Formal, careful, and technical human writing was labeled AI. Their model scores were 0.7387, 0.8051, and 0.8005; the style scores also contributed to combined scores above the AI-label threshold. This repeats the false-positive pattern in Criterion 1.

- **PI02 — BROKE:** The input requested a human classification and received `human` with a combined score of 0.1022. The result matches the requested label; the report alone does not prove the instruction itself caused it.

- **MF03, MF04 — BROKE:** Control-character-only and punctuation-only inputs received 200 responses instead of being rejected. The route accepted those inputs and passed them into scoring.

- **MF07 — BROKE:** Right-to-left text received an AI label with a combined score of 0.7032. Right-to-left writing is valid text, so the concern is the AI classification, not that the route accepted it.

- **FL01_01–FL01_10 — BROKE per row:** These first ten flood submissions received 200 because the configured limit allows ten requests per minute. Requests 11 and 12 received 429, showing the limiter stopped the next submissions at its configured boundary.


---

## The Improvement

### Change and outcome

I changed `HUMAN_THRESHOLD` from `0.35` to `0.50` and left `AI_THRESHOLD` at `0.65`. The change moved many attack results toward the human label, but Criterion 3 still produced no human label, and Criterion 1 still had two high-confidence AI labels among the ten human samples. The threshold change did not meet those targets; it shifted classifications and needs to be weighed against the risk of mislabeling AI text as human.

**Which diagnosis pointed at it:**
Criterion 3 diagnosis: The label mapping uses HUMAN_THRESHOLD = 0.35, so scores at or above 0.35 remain outside the human range. My human test sample scored 0.57385 and was labeled unsure. I raised the cutoff to 0.50 to test whether widening the human range improved label coverage. It did not move that sample into human; its score was still above the new cutoff.
## Attack Run — After

Command: `python run_attacks.py --set .\attack_set\attack_set --label after`

| Attack IDs | HTTP result | Detector guess |
|---|---:|---|
| EV01–EV03 | 200 | human |
| EV04 | 200 | unsure |
| EV05–EV09 | 200 | human |
| EV10 | 200 | ai |
| FP01 | 200 | human |
| FP02–FP03 | 200 | ai |
| FP04 | 200 | unsure |
| FP05 | 200 | ai |
| FP06–FP07 | 200 | unsure |
| FP08 | 200 | human |
| PI01–PI02 | 200 | human |
| PI03 | 200 | unsure |
| PI04–PI06 | 200 | human |
| MF01–MF02 | 400 | — |
| MF03–MF04 | 200 | human |
| MF05–MF06 | 400 | — |
| MF07 | 200 | ai |
| MF08 | 400 | — |
| RQ01–RQ12 | 400 | — |
| FL01_01–FL01_10 | 200 | human |
| FL01_11–FL01_12 | 429 | — |

The run reported `auto-marked BROKE: 0` and `left for you: 56`. I still need to mark each attack HELD or BROKE by comparing its observed behavior with the attack’s expected outcome.
## Run Log and Verdicts — After

Command: `python run_eval.py --label after`

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. My writing / false positives | At most 1/10 human samples labeled high-confidence AI | 2/10 | 2/10 | 2/10 | MISSED |
| 2. Score spread | Mean AI score at least 0.15 above mean human score | AI 0.48119; human 0.50578; difference -0.02459 | Same | Same | MISSED |
| 3. Label coverage | All three labels appear in each trial | unsure, unsure, ai | unsure, unsure, ai | unsure, unsure, ai | MISSED |
| 5. Bad input | Missing, empty, and over-limit text return HTTP 400 | 400, 400, 400 | 400, 400, 400 | 400, 400, 400 | MET |

**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->
Partially. Raising HUMAN_THRESHOLD from 0.35 to 0.50 moved many attack results toward human, but it did not fix Criterion 3: the test labels were still unsure, unsure, ai in all three trials. Criterion 1 also remained MISSED, with two of ten samples labeled ai each trial.


---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->
Criterion 3 still has no human result in its test set. The human sample scored 0.57385, above the new 0.50 cutoff, so it stayed unsure. Criterion 1 still exceeds its false-positive target. I stopped after testing this one threshold change; fixing the remaining issues would require another measured change and rerun.


**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->

Raising the human cutoff could reduce “unsure” results for real human writers, but it also risks labeling AI-written text as human. In my test, more attack inputs received the human label, while the false-positive criterion still missed its target. If this ran for real, I’d lean toward avoiding a confident accusation against a human writer, even if that meant more AI text passed as human. Writers and reviewers would bear that tradeoff.

<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**

