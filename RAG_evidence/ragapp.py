import streamlit as st

from rag_pipeline import run_rag_fact_check
from llm_summary import generate_fact_check_summary


# -------------------------
# Page Config
# -------------------------
st.set_page_config(
    page_title="Fake News Fact Checker",
    page_icon="📰",
    layout="centered"
)


# -------------------------
# UI
# -------------------------
st.title("📰 Fake News Fact Checker")

st.markdown("Enter a claim below and verify whether it is true or false.")


claim = st.text_input(
    "Enter a claim to fact-check",
    placeholder="Type your claim here..."
)


check_btn = st.button("Check")


# -------------------------
# Processing
# -------------------------
if check_btn:

    if not claim.strip():
        st.warning("⚠️ Please enter a claim")
    else:

        with st.spinner("Checking... please wait ⏳"):

            try:
                # Step 2–5: RAG pipeline
                urls, evidence = run_rag_fact_check(claim)

                # Step 6: LLM verdict
                result = generate_fact_check_summary(
                    claim,
                    evidence,
                    urls
                )

                # -------------------------
                # Output
                # -------------------------
                st.success("✅ Fact-check completed")

                st.subheader("📝 Claim")
                st.write(claim)

                st.subheader("📊 Result")
                st.text(result)

                st.subheader("🔗 Sources")

                if urls:
                    for url in urls:
                        st.markdown(f"- [{url}]({url})")
                else:
                    st.write("No sources found")

            except Exception as e:
                st.error("❌ Something went wrong")
                st.exception(e)


# -------------------------
# Footer
# -------------------------
st.markdown("---")
st.caption("Fake News Detection System using RAG + LLM")
