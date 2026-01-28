from google import genai
from decouple import config

PROJECT_ID = config("PROJECT_ID") 
REGION = config("REGION") 
MODEL_NAME = config("MODEL_NAME")

client = genai.Client(vertexai=True, project=PROJECT_ID, location=REGION)
response = client.models.generate_content(
    model=MODEL_NAME,
    contents="Você é uma inteligência artificial?",
)
print({"Você é uma inteligência artificial?": response.text})