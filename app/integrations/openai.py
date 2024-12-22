import logging
import os

import requests

api_key = os.getenv("OPENAI_API_KEY")


def get_openai_answer(question):
    api_url = "https://api.openai.com/v1/chat/completions"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}

    payload = {
        "model": "gpt-4",
        "messages": [
            {
                "role": "system",
                "content": "Provide a response based on the given question.",
            },
            {"role": "user", "content": question},
        ],
        "temperature": 0.7,
    }

    try:
        response = requests.post(api_url, headers=headers, json=payload)
        if response.status_code == 200:
            api_response = (
                response.json()
                .get("choices", [{}])[0]
                .get("message", {})
                .get("content", "")
            )
            return api_response.strip()
        else:
            logging.error(f"API Error {response.status_code}")
            return None
    except Exception as e:
        logging.error(f"API call error while fetching answer: {str(e)}")
        return None
