from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination
from agents.code_executor_agent import getCodeExecutorAgent
from agents.code_generating_agent import code_generator_agent


def getSoftwareDevelopmentTeam(docker, model_client):

    code_executor_agent = getCodeExecutorAgent(docker)

    data_analyzer_agent = code_generator_agent(model_client)

    text_mention_termination = TextMentionTermination("STOP")

    team = RoundRobinGroupChat(
        participants=[data_analyzer_agent, code_executor_agent],
        max_turns=2,
        termination_condition=text_mention_termination,
    )
    return team
