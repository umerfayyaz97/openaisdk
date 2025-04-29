import asyncio
from openai import AsyncOpenAI
from agents import Runner, Agent, function_tool, set_tracing_disabled, OpenAIChatCompletionsModel
import os
from dotenv import load_dotenv
load_dotenv()

#disbale tracing (true by default)
set_tracing_disabled(disabled=True)

#setting model and api key
MODEL = "gemini/gemini-2.0-flash"
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

async def main():
    agent = Agent(
        name = "Assistant",
        instructions="Your name is Assistant. You are a helpful assistant.",
        model=OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=client),
    )

    result = await Runner.run(
        agent,
        "What is the capital of France?",
    )

    print(result.final_output)


def call():
    # Call the main function to run the agent
    asyncio.run(main())