from autogen_agentchat.agents import AssistantAgent
from models import open_ai_client


def get_chat_agent():
    agent = AssistantAgent(
        name="chat_agent",
        description="Helps to answer questions during chatbot conversation.",
        model_client=open_ai_client.get_model_client(),
        system_message="You are a helpful assistant that answers questions based on the provided context.",
        tools=[],
    )
    return agent
