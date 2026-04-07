import requests
import json

def generate_answer(context, question):
    prompt = f"""
    Answer the question ONLY using the context.

    Choose the most relevant information from the context.

    Return a short and exact answer.

    Context:
    {context}

    Question:
    {question}

    Answer:
    """
    
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model":"phi",
            "prompt": prompt,
            "stream": False
        }
        
    )
    result = response.text.strip()
    
    try:
        return json.loads(result)["response"]
    except Exception as e:
        return result