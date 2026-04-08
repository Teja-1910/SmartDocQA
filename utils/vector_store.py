import chromadb
import uuid

# ✅ Persistent DB
client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(name="documents")


# 🔹 DELETE OLD COMPANY DATA
def delete_company_data(company_name):
    results = collection.get(where={"company": company_name})

    if results and results["ids"]:
        collection.delete(ids=results["ids"])
        print(f"{company_name} old data deleted.")


# 🔹 CHECK COMPANY EXISTS
def company_exists(company_name):
    results = collection.get(where={"company": company_name})
    return len(results["ids"]) > 0


# 🔹 STORE EMBEDDINGS
def store_embeddings(chunks, embeddings, company_name):
    # Delete old data
    delete_company_data(company_name)

    ids = [str(uuid.uuid4()) for _ in chunks]

    metadatas = [{"company": company_name} for _ in chunks]

    collection.add(
        documents=chunks,
        embeddings=embeddings.tolist(),
        ids=ids,
        metadatas=metadatas
    )

    print(f"{company_name} data stored successfully!")


# 🔹 QUERY
def query_embeddings(query_embedding, k=5, company_name=None):
    if company_name:
        results = collection.query(
            query_embeddings=query_embedding.tolist(),
            n_results=k,
            where={"company": company_name}
        )
    else:
        results = collection.query(
            query_embeddings=query_embedding.tolist(),
            n_results=k
        )

    docs = results["documents"][0]

    return docs