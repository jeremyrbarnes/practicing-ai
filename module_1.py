from openai import OpenAI

import os

from dotenv import load_dotenv
load_dotenv()

open_api_key = os.getenv("OPENAI_API_KEY")

openai_client = OpenAI(api_key =open_api_key)
print("OpenAI Client initialized successfully.")

my_message = "Hello, OpenAI! This is a test message from my Python script."
response = openai_client.chat.completions.create(model = "gpt-4o-mini", messages = [{"role": "user", "content": my_message}])
print("Response from OpenAI:", response.choices[0].message.content)
