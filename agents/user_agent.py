from autogen_agentchat.agents import UserProxyAgent


def get_user_proxy_agent():
    """
    Creates a user proxy agent that interacts with the user only during its turn.

    Returns:
        UserProxyAgent instance.
    """
    user_proxy_agent = UserProxyAgent(
        name="user_proxy_agent",
        description="Represents the user who reviews code and provides feedback. If satisfied, responds with 'APPROVE'.",
    )

    # Set system message after initialization if possible
    user_proxy_agent.system_message = """
You are a User Proxy Agent in a multi-agent workflow. Your responsibilities are:

1. Review the code generated and executed by other agents.
2. Provide constructive feedback to improve the code if necessary.
3. Once you are fully satisfied with the code and the result, respond with the message: APPROVE
4. Only respond when it is your turn in the team cycle.
"""
    return user_proxy_agent
