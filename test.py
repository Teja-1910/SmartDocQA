from utils.chunking import chunk_text
from utils.embeddings import get_embeddings
from utils.vector_store import create_faiss_index, search

text = "This is a sample document for testing embeddings and Faiss" *20

chunks = chunk_text(text)

embeddings = get_embeddings(chunks)

index = create_faiss_index(embeddings)

query = ["Sample Document"]

query_vector = get_embeddings(query)

indices = search(index, query_vector)

print("Total chunks: ", len(chunks))
print("Top matching chunk indices: ", indices)

for i in indices[0]:
    print("Matched_chunk:\n", chunks[i])