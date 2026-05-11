from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load knowledge
with open("data/knowledge.txt", "r") as f:
    documents = f.readlines()

# Convert to embeddings
doc_embeddings = model.encode(documents)

# Create FAISS index
dimension = doc_embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(doc_embeddings))


def retrieve(query):
    query_embedding = model.encode([query])
    distances, indices = index.search(np.array(query_embedding), k=2)

    results = [documents[i] for i in indices[0]]
    return results


# Test
query = "corporate event planning tips"
results = retrieve(query)

print("Relevant Info:")
for r in results:
    print("-", r)