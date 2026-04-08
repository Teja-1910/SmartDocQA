import requests
import json

def generate_answer(context, question):
    prompt = f"""
You are a document question answering system.

Find the MOST relevant answer from the context.

Do NOT guess.
Do NOT use outside knowledge.

Prefer:
- Titles for topic questions
- Exact matching phrases

Return ONLY the final answer.

Context:
{context}

Question:
{question}

Answer:
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "phi",
            "prompt": prompt,
            "stream": False,
            "temperature": 0
        }
    )

    result = response.text.strip()

    try:
        return json.loads(result)["response"]
    except Exception:
        return result