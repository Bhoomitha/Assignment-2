import requests
import os
import json

API_KEY = os.getenv("GOOGLE_API_KEY")

def query_gemini(prompt):

    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent?key={API_KEY}"

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        result = response.json()

        if "candidates" in result:
            return result["candidates"][0]["content"]["parts"][0]["text"]
        else:
            return json.dumps(result, indent=2)

    except Exception as e:
        return str(e)


if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    print("Querying Gemini...")
    answer = query_gemini(user_prompt)
    print("Response:")
    print(answer)