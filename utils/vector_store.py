import chromadb

client = chromadb.Client()

collection = client.get_or_create_collection(name = "documents")

def store_embeddings(chunks, embeddings):
    ids = [ str(i) for i in range(len(chunks))]
    
    collection.add(
        documents = chunks,
        embeddings=embeddings.tolist(),
        ids = ids
    )
    

def query_embeddings(query_embedding, k=3):
    results = collection.query(
        query_embeddings = query_embedding.tolist(),
        n_results=k
    )
    docs =  results['documents'][0]
    print("RETRIEVED DOCS:", docs)
    return docs
            
            
            
            
            
            
            
            
            


