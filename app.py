import streamlit as st
from utils.chunking import chunk_text
from utils.embeddings import get_embeddings
from utils.vector_store import store_embeddings, query_embeddings
from utils.llm import generate_answer
from utils.pdf_loader import load_pdf

st.title("📄 SmartDocQA")

role = st.selectbox("Select Role", ["User", "Admin"])


if role == "Admin":
    uploaded_file = st.file_uploader("Upload PDF", type="pdf")

    if uploaded_file:
        text = load_pdf(uploaded_file)

        chunks = chunk_text(text)
        embeddings = get_embeddings(chunks)

        store_embeddings(chunks, embeddings)

        st.success("PDF processed successfully!")

else:
    st.info("Upload is restricted to Admin only")


question = st.text_input("Ask a question")

if st.button("Get Answer"):

    if question:
        
        
        query_embedding = get_embeddings([question])

        results = query_embeddings(query_embedding)

        context = " ".join(results)

        answer = generate_answer(context, question)

        st.subheader("Answer:")
        st.write(answer)

    else:
        st.warning("Please enter a question")

