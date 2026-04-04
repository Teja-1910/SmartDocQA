import faiss
import numpy as np

def create_faiss_index(embeddings):
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    return index

def search(index,query_vector,k=3):
    distances, indices = index.search(query_vector, k)
    return indices
    