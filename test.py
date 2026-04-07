from utils.chunking import chunk_text
from utils.embeddings import get_embeddings
from utils.vector_store import store_embeddings, query_embeddings
text = "This is a sample document for testing embeddings and Faiss" *20

chunks = chunk_text(text)

embeddings = get_embeddings(chunks)

store_embeddings(chunks, embeddings)

query = "What is the document about?"
query_embedding = get_embeddings([query])

results = query_embeddings(query_embedding)

print("\nTop Results:")
for r in results:
    print(r)