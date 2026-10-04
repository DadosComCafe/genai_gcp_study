import random
import time

from decouple import config
from google import genai
from google.genai import errors

GEMINI_API_KEY = config("GEMINI_API_KEY")
MODEL_NAME = config("MODEL_NAME", default="gemini-3.5-flash")

client = genai.Client(api_key=GEMINI_API_KEY)
chat = client.chats.create(model=MODEL_NAME)


def enviar_com_retry(chat: genai.Client.chats.create, mensagem: str, max_tentativas: int=4) -> genai.Client.chats.create.send_message:
    """Uma função auxiliar que garante que o agente realizará um número mínimo de retry,
    para o caso de indisponibilidade do agente.

    Args:
        chat (genai.Client.chats.create): chat é o objeto Chat retornado por create().
        mensagem (str): Um texto, que será enviado como pergunta ao agente.
        max_tentativas (int, optional): O número de vezes que a função tentará (try) retornar uma mensagem verdadeira
        não nula.. Defaults to 4.

    Returns:
        genai.Client.chats.create.send_message: A resposta do agente.
    """
    for tentativa in range(max_tentativas):
        try:
            return chat.send_message(mensagem)

        except errors.ServerError as erro:
            if erro.code != 503:
                raise

            if tentativa == max_tentativas - 1:
                print("\nGemini está indisponível no momento. Tente novamente mais tarde.")
                return None

            espera = (2 ** tentativa) + random.uniform(0, 1)
            print(
                f"\nServiço temporariamente ocupado. "
                f"Tentando novamente em {espera:.1f} segundos..."
            )
            time.sleep(espera)


while True:
    mensagem = input("Você: ").strip()

    if mensagem.lower() in {"sair", "exit"}:
        print("Conversa encerrada.")
        break

    if not mensagem:
        continue

    resposta = enviar_com_retry(chat, mensagem)

    if resposta:
        print("Gemini:", resposta.text)