import streamlit as st
import asyncio

from teams.software_development_team import getSoftwareDevelopmentTeam
from models.open_ai_client import get_model_client
from config.docker_util import (
    getDockerCommandLineExecutor,
    start_docker_container,
    stop_docker_container,
)
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.base import TaskResult


st.title("Code Generation and Execution App ")


if "messages" not in st.session_state:
    st.session_state.messages = []
if "autogen_team_state" not in st.session_state:
    st.session_state.autogen_team_state = None

task = st.chat_input(
    "Enter the program which you like to execute by multi-agent workflow:"
)


async def run_code_generation_multiagent(docker, openai_model_client, task):
    try:
        await start_docker_container(docker)
        team = getSoftwareDevelopmentTeam(docker, openai_model_client)

        if st.session_state.autogen_team_state is not None:
            await team.load_state(st.session_state.autogen_team_state)

        async for message in team.run_stream(task=task):
            if isinstance(message, TextMessage):
                if message.source.startswith("user_proxy_agent"):
                    with st.chat_message("user", avatar="👤"):
                        st.markdown(message.content)
                elif message.source.startswith("code_generator_agent"):
                    with st.chat_message("code generator", avatar="🤖"):
                        st.markdown(message.content)
                elif message.source.startswith("Python_Code_Executor"):
                    with st.chat_message("code executor", avatar="👨‍💻"):
                        st.markdown(message.content)
                st.session_state.messages.append(message.content)
                # st.markdown(f"{message.content}")
            elif isinstance(message, TaskResult):
                st.markdown(f"Stop Reason :{message.stop_reason}")

                st.session_state.messages.append(message.stop_reason)
        st.session_state.autogen_team_state = await team.save_state()
        return None

    except Exception as e:
        st.error(f"Error: {e}")
        return e
    finally:
        await stop_docker_container(docker)


if st.session_state.messages:
    for msg in st.session_state.messages:
        st.markdown(msg)

if task:
    openai_model_client = get_model_client()
    docker = getDockerCommandLineExecutor()

    error = asyncio.run(
        run_code_generation_multiagent(docker, openai_model_client, task)
    )
    if error:
        st.error(f"An error occured: {error}")
