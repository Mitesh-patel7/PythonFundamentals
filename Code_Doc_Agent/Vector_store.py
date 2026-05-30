import chromadb

client = chromadb.Client()

collection = client.create_collection(name="codebase")

def store_chunk(id, content):

    collection.add(
        ids=[id],
        documents=[content]
    )

def search_codebase(query):

    results = collection.query(
        query_texts=[query],
        n_results=5
    )

    return results