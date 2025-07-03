from keys import apiKey
import google.generativeai as genai
import os
from promtEngineering import get_promt

# Set the API key
genai.configure(api_key=apiKey)

# Create a generative model
model = genai.GenerativeModel("gemini-1.5-flash")


def generate_content(prompt):
    response = model.generate_content(prompt)
    return response.text


if __name__ == "__main__":
    while True:
        prompt = get_promt()
        if prompt:
            response = generate_content(prompt)
            print(response)
        else:
            print("No prompt found")
