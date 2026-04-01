from utils.chunking import chunk_text
from utils.embeddings import get_embeddings

text = "This is a sample document for testing embeddings"*20

chunks = chunk_text(text)

embeddings = get_embeddings(chunks)

print("Chunks: ",len(chunks))
print("Embeddings: ", embeddings.shape)