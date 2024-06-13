from openai import OpenAI
import os

def ask_gpt(text=0):
    if text == 0:
        text = input("Enter text: ")
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    response = client.chat.completions.create(
    messages=[
            {
                "role": "user",
                "content": text,
            }
        ],
        model="gpt-4",
    )
    print("Response text: " + response.choices[0].message.content)

ask_gpt()