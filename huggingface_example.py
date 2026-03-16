import requests
import os
import json

API_KEY = os.getenv("HUGGINGFACE_API_KEY")

def query_huggingface(prompt):

    url = "https://api-inference.huggingface.co/models/gpt2"

    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }

    data = {
        "inputs": prompt
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        result = response.json()

        return json.dumps(result, indent=2)

    except Exception as e:
        return str(e)


if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    print("Querying HuggingFace...")
    answer = query_huggingface(user_prompt)
    print("Response:")
    print(answer)