from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig
import os
from dotenv import load_dotenv
load_dotenv()
from agents import set_default_openai_client

from dotenv import load_dotenv
load_dotenv()

#setting model and api key
MODEL = "gemini/gemini-2.0-flash"
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

# Set the default OpenAI client with the API key and base URL

external_client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

set_default_openai_client(external_client)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client,
)

agent = Agent(name="Assistant", instructions="Your name is Assistant. You are a helpful assistant.",)

result = Runner.run_sync(agent, "What is the capital of France?")

print(result.final_output)