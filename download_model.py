import os
from sentence_transformers import SentenceTransformer

os.makedirs("./models", exist_ok=True)
model_path = './models/all-MiniLM-L6-v2'

if not os.path.exists(model_path):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    model.save(model_path)
    print("✅ Embedding model saved to", model_path)
else:
    print("Model already exists.")
