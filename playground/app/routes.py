from fastapi import FastAPI
from app.decorators.decorators import agent_endpoint

app = FastAPI()

@app.get("/")
def read_root():
    return {"Very simple": "Server"}

@agent_endpoint("hello_world")
def hello_world_agent(prompt: str):
    response = f"Você fez a seguinte pergunta: {prompt}"
    return {"response": response}