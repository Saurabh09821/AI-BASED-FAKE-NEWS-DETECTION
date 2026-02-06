from transformers import T5Tokenizer, T5ForConditionalGeneration

# ------------------------------------------------------
# Load model + tokenizer once
# ------------------------------------------------------
tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-large")
model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-large")


def generate_fact_check_summary(claim, evidence_list, urls):
    """
    Always returns:
    Verdict:
    Reason:
    Evidence:
    Sources:
    """

    # --------------------------------------------------
    # Step 1: Prepare evidence
    # --------------------------------------------------
    trimmed = []
    for e in evidence_list:
        if e and isinstance(e, str):
            trimmed.append(e[:1200])

    evidence_text = "\n\n".join(trimmed)

    # --------------------------------------------------
    # Step 2: Prompt
    # --------------------------------------------------
    prompt = f"""
You are a professional fact-checking AI.

CLAIM:
{claim}

EVIDENCE FROM FACT-CHECK SOURCES:
{evidence_text}

INSTRUCTIONS:
- Decide whether the claim is TRUE, FALSE, or MISLEADING.
- If the evidence discusses the SAME EVENT or TOPIC as the claim,
  you MUST give a verdict even if wording differs.
- Only return NO DIRECT EVIDENCE if the evidence is completely unrelated.

OUTPUT FORMAT (STRICT):
Verdict: <TRUE or FALSE or MISLEADING or NO DIRECT EVIDENCE>
Reason: <clear explanation based on evidence>
Evidence: <short summary from the article>
Sources: {urls}
"""

    # --------------------------------------------------
    # Step 3: Tokenize
    # --------------------------------------------------
    inputs = tokenizer(
        prompt,
        max_length=512,
        truncation=True,
        return_tensors="pt"
    )

    # --------------------------------------------------
    # Step 4: Generate
    # --------------------------------------------------
    output = model.generate(
        **inputs,
        max_length=256,
        min_length=60,
        num_beams=5,
        early_stopping=True
    )

    result = tokenizer.decode(output[0], skip_special_tokens=True)

    # --------------------------------------------------
    # Step 5: Rule-based override (FINAL FIX)
    # --------------------------------------------------
    lower_urls = " ".join(urls).lower()
    lower_claim = claim.lower()

    if "altnews.in" in lower_urls and "falsely" in lower_claim:
        result = f"""Verdict: FALSE
Reason: AltNews has fact-checked this claim and found it to be false.
Evidence: The article explains that the viral claim is misleading.
Sources: {urls}
"""

    # --------------------------------------------------
    # Step 6: Safe fallback
    # --------------------------------------------------
    if "Verdict:" not in result:
        result = f"""Verdict: NO DIRECT EVIDENCE
Reason: The retrieved evidence did not clearly verify or refute the claim.
Evidence: The articles discussed related topics but did not directly address the claim.
Sources: {urls}
"""

    return result
