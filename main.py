import asyncio
from teams.software_development_team import getSoftwareDevelopmentTeam
from models.open_ai_client import get_model_client
from config.docker_util import (
    getDockerCommandLineExecutor,
    start_docker_container,
    stop_docker_container,
)
from autogen_agentchat.messages import TextMessage


async def main():

    openai_model_client = get_model_client()
    docker = getDockerCommandLineExecutor()

    team = getSoftwareDevelopmentTeam(docker, openai_model_client)

    try:
        task = "check two numbers are polyndromic or not"

        await start_docker_container(docker)

        async for message in team.run_stream(task=task):
            if isinstance(message, TextMessage):
                print(f"message.source: {message.source}")
                print(f"message.content: {message.content}")

    except Exception as e:
        print(e)
    finally:
        await stop_docker_container(docker)


if __name__ == "__main__":
    asyncio.run(main())
