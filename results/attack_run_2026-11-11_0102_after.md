# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-11 01:02
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `264335c577d64498987075ed38ffb31d` | human | 0.382 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `f170670f3e94481ebd0147a3ea3b4aa4` | human | 0.307 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `c0f5bc4899d74e178af97cbcf570032f` | human | 0.469 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `012ee6ebc1594bd9940fe3a2f6dd6cee` | unsure | 0.599 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `6607a6fc4be2495f9b61d3f2c0cf7274` | human | 0.181 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `bda432e0c106481480c162d4920e9d8c` | human | 0.367 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `1b562654e7124ce0af93d61a18eda802` | human | 0.418 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `e04b5a87eae3442588946f18a8ffecef` | human | 0.452 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `6db8fb5459a147ae9fa6210d2b9c288c` | human | 0.500 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `1dc7f29d80924adfbdfa5d8b42f237ea` | ai | 0.732 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `dea71d4dfe19449f8492d142f0dcfb5b` | human | 0.489 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `f259099ba69241f4a54a848942d6d80d` | ai | 0.665 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `19cfb1a15dd64706bf08c35230a1d662` | ai | 0.664 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `e26e58e9183d4fa987ec987c7c132170` | unsure | 0.622 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `82529b9e8f1a4c45b4c5fe308b4bf97f` | ai | 0.734 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `c6c65ab97311478d882e2abc4524fa0f` | unsure | 0.584 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `6d7d8ec00a354ccfbab0dcef987a6465` | unsure | 0.543 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `533bfae4ead949a49189b3a03e5fa0d0` | human | 0.407 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `b096cdb83efa453294e3a70dd1b0c450` | human | 0.295 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `c28052e936294c4bba1613777a3ddaaf` | human | 0.102 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `77f8f9267175417fb0e135ebcc27666b` | unsure | 0.520 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `378ed68d0b6b436eb12d21ee91bcc27b` | human | 0.391 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `5191d091cfac4656a0fa277d2569faf7` | human | 0.419 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `ba5bfcb72acc4c2c81e32cd09d173a2c` | human | 0.466 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `a75e3969f8824ae8bc0704a5700f3612` | human | 0.250 |  |
| MF04 | malformed | text is only punctuation | 200 | `8170a9cb523643de9f6e08fd4af6c637` | human | 0.381 |  |
| MF05 | malformed | text is a very long single word | 400 | `—` | — | — |  |
| MF06 | malformed | text is emoji only | 400 | `—` | — | — |  |
| MF07 | malformed | text is right-to-left script | 200 | `3212d063e6a749b0a04dfc5b2937a723` | ai | 0.703 |  |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `bc7ff0af7e1c4b4f940d0706b3c0f0e6` | human | 0.264 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `47b1af9c2df64249a573ab825ff94475` | human | 0.264 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `6c5b43f76bcb456ea9fb28b12c04fd6c` | human | 0.264 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `fdb6fc06bb7f47d1be1db329750870f3` | human | 0.264 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `629aa0b1c8914572ab25901f119637ee` | human | 0.264 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `4c764cdcafd9461bb20fc90ad0e46a8d` | human | 0.264 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `8f184a8815d149aab7562d2d495f10ec` | human | 0.264 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `e81aaea841424201af149ed4580d06a8` | human | 0.264 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `6ff0005ba6d849c3a4f3350b444487a5` | human | 0.264 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `d9641ae81559483f953131d0490937eb` | human | 0.264 |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "264335c577d64498987075ed38ffb31d",
  "creator_id": "attacker_EV01",
  "guess": "human",
  "confidence": 0.38215,
  "model_score": 0.1635,
  "style_score": 0.6008,
  "label": "This writing appears more likely to have been written by a person. This result is an estimate, not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "f170670f3e94481ebd0147a3ea3b4aa4",
  "creator_id": "attacker_EV02",
  "guess": "human",
  "confidence": 0.30655000000000004,
  "model_score": 0.5943,
  "style_score": 0.0188,
  "label": "This writing appears more likely to have been written by a person. This result is an estimate, not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "c0f5bc4899d74e178af97cbcf570032f",
  "creator_id": "attacker_EV03",
  "guess": "human",
  "confidence": 0.46945000000000003,
  "model_score": 0.6662,
  "style_score": 0.2727,
  "label": "This writing appears more likely to have been written by a person. This result is an estimate, not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "012ee6ebc1594bd9940fe3a2f6dd6cee",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.5989,
  "model_score": 0.6114,
  "style_score": 0.5864,
  "label": "We couldn't confidently determine whether this writing was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "6607a6fc4be2495f9b61d3f2c0cf7274",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.1815,
  "model_score": 0.3212,
  "style_score": 0.0418,
  "label": "This writing appears more likely to have been written by a person. This result is an estimate, not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "bda432e0c106481480c162d4920e9d8c",
  "creator_id": "attacker_EV06",
  "guess": "human",
  "confidence": 0.3671,
  "model_score": 0.5727,
  "style_score": 0.1615,
  "label": "This writing appears more likely to have been written by a person. This result is an estimate, not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "1b562654e7124ce0af93d61a18eda802",
  "creator_id": "attacker_EV07",
  "guess": "human",
  "confidence": 0.4181,
  "model_score": 0.5862,
  "style_score": 0.25,
  "label": "This writing appears more likely to have been written by a person. This result is an estimate, not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "e04b5a87eae3442588946f18a8ffecef",
  "creator_id": "attacker_EV08",
  "guess": "human",
  "confidence": 0.4516,
  "model_score": 0.2452,
  "style_score": 0.658,
  "label": "This writing appears more likely to have been written by a person. This result is an estimate, not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "6db8fb5459a147ae9fa6210d2b9c288c",
  "creator_id": "attacker_EV09",
  "guess": "human",
  "confidence": 0.4998,
  "model_score": 0.7042,
  "style_score": 0.2954,
  "label": "This writing appears more likely to have been written by a person. This result is an estimate, not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "1dc7f29d80924adfbdfa5d8b42f237ea",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.7319,
  "model_score": 0.9792,
  "style_score": 0.4846,
  "label": "This writing appears more likely to have been generated by AI. This result is an estimate, not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "dea71d4dfe19449f8492d142f0dcfb5b",
  "creator_id": "attacker_FP01",
  "guess": "human",
  "confidence": 0.4892,
  "model_score": 0.6175,
  "style_score": 0.3609,
  "label": "This writing appears more likely to have been written by a person. This result is an estimate, not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "f259099ba69241f4a54a848942d6d80d",
  "creator_id": "attacker_FP02",
  "guess": "ai",
  "confidence": 0.6646000000000001,
  "model_score": 0.7387,
  "style_score": 0.5905,
  "label": "This writing appears more likely to have been generated by AI. This result is an estimate, not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "19cfb1a15dd64706bf08c35230a1d662",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "confidence": 0.66395,
  "model_score": 0.8051,
  "style_score": 0.5228,
  "label": "This writing appears more likely to have been generated by AI. This result is an estimate, not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "e26e58e9183d4fa987ec987c7c132170",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.62215,
  "model_score": 0.8329,
  "style_score": 0.4114,
  "label": "We couldn't confidently determine whether this writing was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "82529b9e8f1a4c45b4c5fe308b4bf97f",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.73395,
  "model_score": 0.8005,
  "style_score": 0.6674,
  "label": "This writing appears more likely to have been generated by AI. This result is an estimate, not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "c6c65ab97311478d882e2abc4524fa0f",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.5835,
  "model_score": 0.8814,
  "style_score": 0.2856,
  "label": "We couldn't confidently determine whether this writing was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "6d7d8ec00a354ccfbab0dcef987a6465",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.5431,
  "model_score": 0.8816,
  "style_score": 0.2046,
  "label": "We couldn't confidently determine whether this writing was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "533bfae4ead949a49189b3a03e5fa0d0",
  "creator_id": "attacker_FP08",
  "guess": "human",
  "confidence": 0.40669999999999995,
  "model_score": 0.3223,
  "style_score": 0.4911,
  "label": "This writing appears more likely to have been written by a person. This result is an estimate, not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "b096cdb83efa453294e3a70dd1b0c450",
  "creator_id": "attacker_PI01",
  "guess": "human",
  "confidence": 0.29475,
  "model_score": 0.4625,
  "style_score": 0.127,
  "label": "This writing appears more likely to have been written by a person. This result is an estimate, not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "c28052e936294c4bba1613777a3ddaaf",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.1022,
  "model_score": 0.2044,
  "style_score": 0.0,
  "label": "This writing appears more likely to have been written by a person. This result is an estimate, not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "77f8f9267175417fb0e135ebcc27666b",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.5196000000000001,
  "model_score": 0.5943,
  "style_score": 0.4449,
  "label": "We couldn't confidently determine whether this writing was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "378ed68d0b6b436eb12d21ee91bcc27b",
  "creator_id": "attacker_PI04",
  "guess": "human",
  "confidence": 0.3906,
  "model_score": 0.4998,
  "style_score": 0.2814,
  "label": "This writing appears more likely to have been written by a person. This result is an estimate, not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "5191d091cfac4656a0fa277d2569faf7",
  "creator_id": "attacker_PI05",
  "guess": "human",
  "confidence": 0.41925,
  "model_score": 0.6401,
  "style_score": 0.1984,
  "label": "This writing appears more likely to have been written by a person. This result is an estimate, not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "ba5bfcb72acc4c2c81e32cd09d173a2c",
  "creator_id": "attacker_PI06",
  "guess": "human",
  "confidence": 0.4661,
  "model_score": 0.5583,
  "style_score": 0.3739,
  "label": "This writing appears more likely to have been written by a person. This result is an estimate, not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "a75e3969f8824ae8bc0704a5700f3612",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.25,
  "model_score": 0.0,
  "style_score": 0.5,
  "label": "This writing appears more likely to have been written by a person. This result is an estimate, not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "8170a9cb523643de9f6e08fd4af6c637",
  "creator_id": "attacker_MF04",
  "guess": "human",
  "confidence": 0.3806,
  "model_score": 0.0112,
  "style_score": 0.75,
  "label": "This writing appears more likely to have been written by a person. This result is an estimate, not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF06",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "3212d063e6a749b0a04dfc5b2937a723",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.7032,
  "model_score": 0.9064,
  "style_score": 0.5,
  "label": "This writing appears more likely to have been generated by AI. This result is an estimate, not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "bc7ff0af7e1c4b4f940d0706b3c0f0e6",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.26435,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "This writing appears more likely to have been written by a person. This result is an estimate, not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "47b1af9c2df64249a573ab825ff94475",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.26435,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "This writing appears more likely to have been written by a person. This result is an estimate, not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "6c5b43f76bcb456ea9fb28b12c04fd6c",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.26435,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "This writing appears more likely to have been written by a person. This result is an estimate, not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "fdb6fc06bb7f47d1be1db329750870f3",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.26435,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "This writing appears more likely to have been written by a person. This result is an estimate, not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "629aa0b1c8914572ab25901f119637ee",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.26435,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "This writing appears more likely to have been written by a person. This result is an estimate, not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "4c764cdcafd9461bb20fc90ad0e46a8d",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.26435,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "This writing appears more likely to have been written by a person. This result is an estimate, not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "8f184a8815d149aab7562d2d495f10ec",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.26435,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "This writing appears more likely to have been written by a person. This result is an estimate, not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 200,
  "content_id": "e81aaea841424201af149ed4580d06a8",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.26435,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "This writing appears more likely to have been written by a person. This result is an estimate, not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 200,
  "content_id": "6ff0005ba6d849c3a4f3350b444487a5",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.26435,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "This writing appears more likely to have been written by a person. This result is an estimate, not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 200,
  "content_id": "d9641ae81559483f953131d0490937eb",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.26435,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "This writing appears more likely to have been written by a person. This result is an estimate, not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
