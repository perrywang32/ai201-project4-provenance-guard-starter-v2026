1. Submission path
1. A writer sends [text] and [creator_id] to POST /submit.
2. app.py receives the request and reads the JSON.
3. detector.model_signal(text) checks perplexity to estimate how predictable the text is to the language model, converts that into a score from 0 to 1; higher means more AI-like. Its blind spot is that predictable writing can still be human-written. The signal measures predictability, not authorship.
4. stylometry.style_signal(text) checks the text’s shape: how much sentence lengths vary, how much vocabulary repeats, and how punctuation is used. AI writing may have more regular sentence lengths and less vocabulary variation, though that isn’t true of every writer. The signal can’t understand meaning or determine who wrote something; edits to sentence structure or punctuation can change its score.
5. scoring combines the scores and chooses a an ai, human, or unsure guess and a plain-language label.
6. audit.log_decision(...) records the decision in logs/audit.jsonl.
7. The service returns content_id, guess, confidence (the combined score), label, model_score, and style_score to the writer. Staff can inspect recent entries with GET /log.
2. The two signals and their blind spots
- Model signal: It measures predictability. It can mistake predictable writing for AI-like because it cannot determine predictable writing as human-written.
- Style signal: It measures sentence-length variation, vocabulary repetition, and punctuation. It cannot determine the text’s meaning or who wrote it, and changing sentence lengths or punctuation can affect its score.
3. False-positive example
A writer submits plain human writing with short, conventional sentences. The system gives it an AI-like score and shows the writer an AI-like label. The writer can appeal by sending the content_id from the submission response and their reason for disputing the result to POST /appeal. The system should record the appeal and set the status to under_review.
4. Endpoint shapes
- POST /submit receives: text, creator_id. It returns: content_id, guess, confidence, label, model_score, style_score.
- POST /appeal receives: content_id, reasoning. It should confirm the appeal and record under_review.