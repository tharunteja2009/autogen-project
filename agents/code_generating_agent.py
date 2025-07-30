from autogen_agentchat.agents import AssistantAgent


def code_generator_agent(model_client):
    agent = AssistantAgent(
        name="code_generator_agent",
        description="An agent that generates code based on user prompts.",
        model_client=model_client,
        system_message="""
        You are a code generation agent. 
        1. Code should be like below, in a single block and no multiple block. code should be in python. code should be executable,clean and easy to understand.
        ```python
        your-code-here
        ```
        2. You will receive output of code from another executor agent, if you found any error in the code, you can fix it and send it back to the executor agent.
        3. If any library is not installed in the env, please make sure to do the same by providing the bash script and use pip to install(like pip install matplotlib pandas) and after that send the code again without changes , install the required libraries.
        example
            ```bash
            pip install pandas numpy matplotlib
            ```
       
        4. If the code ran successfully, then analyze the output and continue as needed. 

        Once we have completed all the task, please mention 'STOP' after explaning in depth the final answer.
 """,
    )
    return agent
