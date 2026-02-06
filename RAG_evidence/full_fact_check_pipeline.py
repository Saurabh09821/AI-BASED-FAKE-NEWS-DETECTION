from rag_pipeline import run_rag_fact_check
from llm_summary import generate_fact_check_summary


def fact_check(claim):
    # Step 2–5: Get URLs + evidence using RAG pipeline
    urls, evidence = run_rag_fact_check(claim)

    # Step 6: LLM summary + verdict
    verdict = generate_fact_check_summary(claim, evidence, urls)

    return verdict


if __name__ == "__main__":
    claim = "Italian rhythmic gymnasts video falsely viral as Indian athlete"

    final_output = fact_check(claim)

    print("\n================== FINAL FACT-CHECK RESULT ==================")
    print(final_output)
    print("============================================================")



#🔢 Step 4: Generating embeddings...

#================== FINAL FACT-CHECK RESULT ==================
#Verdict: FALSE
#Reason: AltNews has fact-checked this claim and found it to be false.
#Evidence: The article explains that the viral claim is misleading.
#Sources: ['https://www.altnews.in/italian-rhythmic-gymnasts-video-falsely-viral-as-indian-athlete-shubhashree-more/']

#============================================================

