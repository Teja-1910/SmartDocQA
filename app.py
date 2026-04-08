import streamlit as st
from utils.chunking import chunk_text
from utils.embeddings import get_embeddings
from utils.vector_store import store_embeddings, query_embeddings, company_exists
from utils.llm import generate_answer
from utils.pdf_loader import load_pdf

st.title("📄 SmartDocQA - Centralized Company Knowledge System")

role = st.selectbox("Select Role", ["User", "Admin"])


# ================= ADMIN =================
if role == "Admin":
    st.subheader("📤 Upload  Document(*Ensure that pdf is saved with company name)")

    uploaded_file = st.file_uploader("Upload PDF", type="pdf")

    if uploaded_file:
        # 🔥 AUTO COMPANY NAME
        company_name = uploaded_file.name.split(".")[0]

        text = load_pdf(uploaded_file)
        chunks = chunk_text(text)
        embeddings = get_embeddings(chunks)

        store_embeddings(chunks, embeddings, company_name)

        st.success(f"{company_name} document stored successfully!")


# ================= USER =================
else:
    st.subheader("🔍 Ask Questions")

    st.info("💡 Ask questions like: leave policy, test date, methodology")

    company_name = st.text_input("Enter Company Name")
    question = st.text_input("Enter your question")

    if st.button("Get Answer"):

        if question and company_name:

            # 🔥 VALIDATION
            if not company_exists(company_name):
                st.error(
                    "⚠️ The requested company data is not available. "
                    "Please verify the company name or contact the administrator."
                )

            else:
                query_embedding = get_embeddings([question])

                results = query_embeddings(
                    query_embedding,
                    company_name=company_name
                )

                context = " ".join(results)

                answer = generate_answer(context, question)

                st.subheader("📌 Answer:")
                st.write(answer)

        else:
            st.warning("Please enter both company name and question")