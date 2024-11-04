from dotenv import load_dotenv
import openai
import os
load_dotenv()

api_key = os.getenv("API_KEY")
openai.api_key = os.getenv("API_KEY")

question = input("Fråga mig: ")
response = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = [
        {"role": "system", "content": "You think you are always right, harsh and desicive. Low regards for weakness"},
        {"role": "user", "content": question},
    ],

)
print(response["choices"][0]["message"]["content"])


