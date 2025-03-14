import openai

from agents import Agent, Runner, WebSearchTool, trace

import os
from dotenv import load_dotenv

import agentops

from date import time_now

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

AGENTOPS_API_KEY = os.getenv("AGENTOPS_API_KEY")
agentops.init(AGENTOPS_API_KEY, default_tags=["chat_simulation"])

instructions = f"You are an extremely financially-literate agent that is up to date ({time_now()}) with the Nasdaq and NYSE markets and their stocks."


async def run_web_agent(name, prompt):
    agent = Agent(
        name=f"{name} Search",
        instructions=instructions,
        tools=[WebSearchTool(user_location={"type": "approximate", "city": "New York"}, search_context_size="high")]
    )

    prompt = prompt + f" Today is {time_now()}, so make sure your research is up-to-date."
    with trace(f"{name} Actual Search"):
        result = await Runner.run(
            agent,
            prompt,
        )
        return result.final_output