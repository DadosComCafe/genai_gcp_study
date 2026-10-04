import os
from google import genai
from decouple import config

GEMINI_API_KEY = config("GEMINI_API_KEY")
MODEL_NAME = config("MODEL_NAME")
os.getenv(GEMINI_API_KEY)

client = genai.Client(api_key=GEMINI_API_KEY)
chat = client.chats.create(model=MODEL_NAME)

while True:
    mensagem = input("Você: ")
    if mensagem.lower() in {"sair", "exit"}:
        break

    resposta = chat.send_message(mensagem)
    print("Gemini:", resposta.text)