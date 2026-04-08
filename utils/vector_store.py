import chromadb
import uuid

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(name="documents")


# 🔹 STORE WITH METADATA
def store_embeddings(chunks, embeddings, file_name):
    ids = [str(uuid.uuid4()) for _ in chunks]

    metadatas = [{"source": file_name} for _ in chunks]

    collection.add(
        documents=chunks,
        embeddings=embeddings.tolist(),
        ids=ids,
        metadatas=metadatas
    )

    print(f"{file_name} stored with {len(chunks)} chunks!")


# 🔹 QUERY WITH OPTIONAL FILTER
def query_embeddings(query_embedding, k=5, file_name=None):
    if file_name:
        results = collection.query(
            query_embeddings=query_embedding.tolist(),
            n_results=k,
            where={"source": file_name}   # 🔥 FILTER
        )
    else:
        results = collection.query(
            query_embeddings=query_embedding.tolist(),
            n_results=k
        )

    docs = results['documents'][0]

    print("==== RETRIEVED CHUNKS ====")
    for i, doc in enumerate(docs):
        print(f"\nChunk {i+1}:\n{doc}")
    print("==========================")

    return docs