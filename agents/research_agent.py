from autogen_agentchat.agents import AssistantAgent
from models import open_ai_client
from langchain_community.utilities import GoogleSerperAPIWrapper
from dotenv import load_dotenv
import os

load_dotenv()

google_search = GoogleSerperAPIWrapper(type="search", num_results=3)
os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")


def web_search_tool(query: str) -> str:
    """Query must be a string"""
    return google_search.run(query)


def do_research():
    agent = AssistantAgent(
        name="web_search_agent",
        description="An agent that performs web searches to answer questions in 30 words or less.",
        model_client=open_ai_client.get_model_client(),
        system_message="You are a research agent that can search the web to find information. Use the web search tool to answer questions. in 100 words",
        tools=[web_search_tool],
    )
    return agent
