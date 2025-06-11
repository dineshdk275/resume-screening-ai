from sentence_transformers import SentenceTransformer, util
import numpy as np

# Load pre-trained model once
model = SentenceTransformer('all-MiniLM-L6-v2')  # Lightweight, fast, good performance

def embed_text(text):
    # Embed a single text string
    return model.encode(text, convert_to_tensor=True)

def match_resume(resume_text, job_desc):
    # Get embeddings
    resume_emb = embed_text(resume_text)
    job_emb = embed_text(job_desc)

    # Compute cosine similarity (value between 0 and 1)
    similarity = util.pytorch_cos_sim(resume_emb, job_emb).item()

    # Convert similarity to percentage score out of 100
    score = round(similarity * 100, 2)

    return score
