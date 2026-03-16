import requests
import os
import json

API_KEY = os.getenv("COHERE_API_KEY")

def query_cohere(prompt):

    url = "https://api.cohere.ai/v1/generate"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "command",
        "prompt": prompt,
        "max_tokens": 200
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        result = response.json()

        if "generations" in result:
            return result["generations"][0]["text"]
        else:
            return json.dumps(result, indent=2)

    except Exception as e:
        return str(e)


if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    print("Querying Cohere...")
    answer = query_cohere(user_prompt)
    print("Response:")
    print(answer)