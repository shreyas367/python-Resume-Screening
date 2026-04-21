from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# load once (global, not inside function)
model = SentenceTransformer("paraphrase-MiniLM-L3-v2")

def match_resume(resume: str, job: str):
    # convert text → embeddings
    embeddings = model.encode([resume, job])

    # compute similarity
    score = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )[0][0]

    return {
        "match_score": float(score)
    }