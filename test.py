from utils.chunking import chunk_text
from utils.embeddings import get_embeddings
from utils.vector_store import store_embeddings, query_embeddings


text = "My name is Brahma Teja , Im studying in CBIt and working for Hyniva Consultancy Services Banglore"

chunks = chunk_text(text)

embeddings = get_embeddings(chunks)

store_embeddings(chunks, embeddings)





query = "Where Brahma Teja is working?"
query_embedding = get_embeddings([query])

results = query_embeddings(query_embedding)

print("\nTop Results:")
for r in results:
    print(r)