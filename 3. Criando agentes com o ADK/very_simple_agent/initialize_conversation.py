import asyncio
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from agent.greeting_agent import greeting_agent


async def main():
    session_service = InMemorySessionService()

    session = await session_service.create_session(
        app_name="meu_app",
        user_id="usuario_001"
    )

    print(f"Sessão criada: {session.id}")
    print("-" * 50)

    runner = Runner(
        agent=greeting_agent,
        app_name="meu_app",
        session_service=session_service
    )

    user_message = types.Content(
        role="user",
        parts=[types.Part.from_text(text="Olá! Tudo bem?")]
    )

    print("Usuário: Olá! Tudo bem?")
    print("Agente: ", end="", flush=True)

    async for event in runner.run_async(
        user_id="usuario_001",
        session_id=session.id,
        new_message=user_message
    ):
        if event.content and event.content.parts:
            for part in event.content.parts:
                if hasattr(part, 'text') and part.text:
                    print(part.text, end="", flush=True)

    print("\n" + "-" * 50)

    second_message = types.Content(
        role="user",
        parts=[types.Part.from_text(text="Pode me contar uma curiosidade interessante?")]
    )

    print("Usuário: Pode me contar uma curiosidade interessante?")
    print("Agente: ", end="", flush=True)

    async for event in runner.run_async(
        user_id="usuario_001",
        session_id=session.id,
        new_message=second_message
    ):
        if event.content and event.content.parts:
            for part in event.content.parts:
                if hasattr(part, 'text') and part.text:
                    print(part.text, end="", flush=True)

    print()

if __name__ == "__main__":
    asyncio.run(main())