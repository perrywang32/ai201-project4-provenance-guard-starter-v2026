# Attack run — before

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-10 02:10
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
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `1a318136a9d143eebb3995fddf835546` | unsure | 0.520 | HELD  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `874332958fd44b7f94ce22a768773655` | unsure | 0.391 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `1e8ae23cca094797920f1bcce5e0ec00` | unsure | 0.419 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `a5451b6f1d40464db9c716549d11e4ea` | unsure | 0.466 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 400 | `—` | — | — | HELD |
| MF03 | malformed | text is control characters | 200 | `5caf18267a9b4d35bedc297a6669f969` | human | 0.250 | BROKE |
| MF04 | malformed | text is only punctuation | 200 | `1d6a566ba355499c94c571c89e429048` | unsure | 0.381 | BROKE |
| MF05 | malformed | text is a very long single word | 400 | `—` | — | — | HELD |
| MF06 | malformed | text is emoji only | 400 | `—` | — | — | HELD  |
| MF07 | malformed | text is right-to-left script | 200 | `777a7c02ff1a4e3498b050b1c67c39b1` | ai | 0.703 | BROKE |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — | HELD |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | HELD |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — | HELD |
| RQ03 | malformed | text is a number | 400 | `—` | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | `—` | — | — | HELD |
| RQ05 | malformed | text is null | 400 | `—` | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — | HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | `—` | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — | HELD  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `e1a06d0efe094652ab0f9ff44fab6a24` | human | 0.264 | BROKE  |
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
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD  |

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
  "content_id": "3521803305a54427b8c01e24d1c7126c",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.38215,
  "model_score": 0.1635,
  "style_score": 0.6008,
  "label": "We couldn't confidently determine whether this writing was written by a person or generated by AI.",
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
  "content_id": "9b47867a16914009a515fa6f70dae820",
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
  "content_id": "1508ec7058404d4d9d57465c2df1e137",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.46945000000000003,
  "model_score": 0.6662,
  "style_score": 0.2727,
  "label": "We couldn't confidently determine whether this writing was written by a person or generated by AI.",
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
  "content_id": "303f4ba2b6894c16996955e02109b92f",
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
  "content_id": "9c84c5d75161451cb04e850768e01ed2",
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
  "content_id": "29f6bb937fe64e80bf5654f5b5317819",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.3671,
  "model_score": 0.5727,
  "style_score": 0.1615,
  "label": "We couldn't confidently determine whether this writing was written by a person or generated by AI.",
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
  "content_id": "29007a67a4ad46f38f142eba2b9b8a5f",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.4181,
  "model_score": 0.5862,
  "style_score": 0.25,
  "label": "We couldn't confidently determine whether this writing was written by a person or generated by AI.",
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
  "content_id": "776e56ca0bfa4681985a10c527d1570d",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.4516,
  "model_score": 0.2452,
  "style_score": 0.658,
  "label": "We couldn't confidently determine whether this writing was written by a person or generated by AI.",
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
  "content_id": "daa1b35ffc1e401ea9ae942e77beed91",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.4998,
  "model_score": 0.7042,
  "style_score": 0.2954,
  "label": "We couldn't confidently determine whether this writing was written by a person or generated by AI.",
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
  "content_id": "a8c82ab45bdc4c9ea0e79bc83ee429e0",
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
  "content_id": "7a55cddac788427280584c3056182dbe",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.4892,
  "model_score": 0.6175,
  "style_score": 0.3609,
  "label": "We couldn't confidently determine whether this writing was written by a person or generated by AI.",
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
  "content_id": "09ac83a94c0c4738b08b7cecff528a93",
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
  "content_id": "5603827d166544e9a88c3d6cd91cfdff",
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
  "content_id": "0e756021dff8495d90136c9b9f09a0d1",
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
  "content_id": "008f04a0462c4a97a287522a8d1c002c",
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
  "content_id": "d7310065f4384741b17f49e64d86d878",
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
  "content_id": "3d87eedc13214bc1af065f8ea5810e72",
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
  "content_id": "03ebcda3a95246baabecc3f5d8f5f589",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.40669999999999995,
  "model_score": 0.3223,
  "style_score": 0.4911,
  "label": "We couldn't confidently determine whether this writing was written by a person or generated by AI.",
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
  "content_id": "932493535e404dffa53f30ac3ae248fd",
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
  "content_id": "0b8caddd721c45d89c1773f73b54f453",
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
  "content_id": "1a318136a9d143eebb3995fddf835546",
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
  "content_id": "874332958fd44b7f94ce22a768773655",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.3906,
  "model_score": 0.4998,
  "style_score": 0.2814,
  "label": "We couldn't confidently determine whether this writing was written by a person or generated by AI.",
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
  "content_id": "1e8ae23cca094797920f1bcce5e0ec00",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.41925,
  "model_score": 0.6401,
  "style_score": 0.1984,
  "label": "We couldn't confidently determine whether this writing was written by a person or generated by AI.",
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
  "content_id": "a5451b6f1d40464db9c716549d11e4ea",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.4661,
  "model_score": 0.5583,
  "style_score": 0.3739,
  "label": "We couldn't confidently determine whether this writing was written by a person or generated by AI.",
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
  "content_id": "5caf18267a9b4d35bedc297a6669f969",
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
  "content_id": "1d6a566ba355499c94c571c89e429048",
  "creator_id": "attacker_MF04",
  "guess": "unsure",
  "confidence": 0.3806,
  "model_score": 0.0112,
  "style_score": 0.75,
  "label": "We couldn't confidently determine whether this writing was written by a person or generated by AI.",
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
  "content_id": "777a7c02ff1a4e3498b050b1c67c39b1",
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
  "content_id": "e1a06d0efe094652ab0f9ff44fab6a24",
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
  "content_id": "bfa149a4080646b895ff037ae000b133",
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
  "content_id": "bbaf3fd978ef44d1b944eb8511d195a7",
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
  "content_id": "fe5adafc85a344da873c865cff4002ca",
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
  "content_id": "44d9295866ec4a739a70d695233ba6ae",
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
  "content_id": "a2267cdc88584942b9ab6e97328bc098",
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
  "content_id": "d6620bc61a0e48bc9588399c2963a33e",
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
  "content_id": "b5e8f17c673b4740a620fb6f75135447",
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
  "content_id": "8f6494ca7e54446580affb1522fea346",
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
  "content_id": "c1e5f08c1c6b4d61978ad1b09ccf05eb",
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
