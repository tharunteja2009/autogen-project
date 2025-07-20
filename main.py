import asyncio
from agents import research_agent
from autogen_agentchat.messages import TextMessage


async def main():
    chat_agent_instance = research_agent.do_research()
    result = await chat_agent_instance.run(
        task="How was latest quarterly earnings for HDFC Bank?"
    )
    print("Result:", result)


if __name__ == "__main__":
    asyncio.run(main())
