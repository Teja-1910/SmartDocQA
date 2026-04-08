import requests
import json

def generate_answer(context, question):
    prompt = f"""
You are a document question answering system.

Answer ONLY from the given context.
Do NOT guess.
Do NOT use outside knowledge.

Return short and precise answer.

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
            "stream": False
        }
    )

    result = response.text.strip()

    try:
        return json.loads(result)["response"].strip()
    except:
        return result