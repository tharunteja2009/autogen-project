import asyncio
from agents import chat_agent
from autogen_agentchat.messages import TextMessage


async def main():
    chat_agent_instance = chat_agent.get_chat_agent()
    # result = await chat_agent_instance.run(task="Who are you")

    stream = chat_agent_instance.run_stream(
        task="Give me top 5 Indian EV cars, with brandnames, battery, range, features, price. in short bullet points.",
    )

    async for message in stream:
        if isinstance(message, TextMessage):
            print(f"[{message.source}] {message.content}\n")


if __name__ == "__main__":
    asyncio.run(main())
