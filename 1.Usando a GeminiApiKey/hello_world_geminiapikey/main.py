import os
from google import genai

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="""
    Por favor, explique em português quando o uso das credenciais
    do gemini pela GEMINI_API_KEY é recomendado.
    """
)

print(interaction.outputs[0].text)
