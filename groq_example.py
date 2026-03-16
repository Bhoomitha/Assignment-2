import requests
import os
import json

API_KEY = os.getenv("GROQ_API_KEY")

def query_groq(prompt):

    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        result = response.json()

        if "choices" in result:
            return result["choices"][0]["message"]["content"]
        else:
            return json.dumps(result, indent=2)

    except Exception as e:
        return str(e)


if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    print("Querying Groq...")
    answer = query_groq(user_prompt)
    print("Response:")
    print(answer)