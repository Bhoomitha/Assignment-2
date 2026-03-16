import requests
import json

def query_ollama(prompt):

    url = "http://localhost:11434/api/generate"

    data = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(url, json=data)
        result = response.json()

        return result["response"]

    except Exception as e:
        return str(e)


if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    print("Querying Ollama...")
    answer = query_ollama(user_prompt)
    print("Response:")
    print(answer)