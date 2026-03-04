from google import genai
from decouple import config

PROJECT_ID = config("GOOGLE_CLOUD_PROJECT") 
REGION = config("GOOGLE_CLOUD_LOCATION") 
MODEL_NAME = config("MODEL_NAME")

client = genai.Client(vertexai=True, project=PROJECT_ID, location=REGION)
response = client.models.generate_content(
    model=MODEL_NAME,
    contents="As configurações necessárias para criação de um agente estão ok?",
)
print({"As configurações necessárias para criação de um agente estão ok?": response.text})