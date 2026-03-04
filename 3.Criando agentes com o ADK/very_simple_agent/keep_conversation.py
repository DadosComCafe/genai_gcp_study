import asyncio
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from agent.greeting_agent import greeting_agent

async def main():
    session_service = InMemorySessionService()

    session = await session_service.create_session(
        app_name="sample_agent",
        user_id="usuario_001"
    )

    runner = Runner(
        agent=greeting_agent,
        app_name="sample_agent",
        session_service=session_service
    )

    print(f"--- Chat Iniciado (Sessão: {session.id}) ---")
    print("Digite 'sair' para encerrar.\n")

    while True:
        user_input = input("Você: ")
        
        if user_input.lower() in ["sair", "exit", "quit"]:
            break

        user_message = types.Content(
            role="user",
            parts=[types.Part.from_text(text=user_input)]
        )

        print("Agente: ", end="", flush=True)

        async for event in runner.run_async(
            user_id="usuario_001",
            session_id=session.id,
            new_message=user_message
        ):
            if event.content and event.content.parts:
                for part in event.content.parts:
                    if hasattr(part, 'text') and part.text:
                        print(f"{part.text}", end="", flush=True)
        
        print("\n")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nConversa encerrada pelo usuário.")