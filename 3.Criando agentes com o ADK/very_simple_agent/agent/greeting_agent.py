import vertexai
from decouple import config
from google.adk.agents import Agent
from agent.descriptions import description
from agent.instructions import instruction

vertexai.init(
    project=config("GOOGLE_CLOUD_PROJECT"),
    location=config("GOOGLE_CLOUD_LOCATION", default="us-central1"),
)

greeting_agent = Agent(
    name="greeting_agent",
    model="gemini-2.5-flash",
    description=description,
    instruction=instruction
)