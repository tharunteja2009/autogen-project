from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination
from agents.code_executor_agent import getCodeExecutorAgent
from agents.code_generating_agent import code_generator_agent
from agents.user_agent import get_user_proxy_agent


def getSoftwareDevelopmentTeam(docker, model_client):
    # Avoid variable name shadowing
    executor_agent = getCodeExecutorAgent(docker)
    generator_agent = code_generator_agent(model_client)
    user_proxy_agent = get_user_proxy_agent()

    # Termination conditions
    stop_termination = TextMentionTermination("STOP")
    approve_termination = TextMentionTermination("APPROVE")

    team = RoundRobinGroupChat(
        participants=[generator_agent, executor_agent, user_proxy_agent],
        max_turns=6,
        termination_condition=stop_termination | approve_termination,
    )
    return team
