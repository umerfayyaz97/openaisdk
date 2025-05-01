from agents import Agent, Runner, AsyncOpenAI, set_default_openai_client, set_tracing_disabled, set_default_openai_api
import os
from dotenv import load_dotenv
load_dotenv()


from dotenv import load_dotenv
load_dotenv()


set_tracing_disabled(True)
#setting model and api key
MODEL = "gemini-2.0-flash"
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

set_default_openai_api("chat_completions")
# Set the default OpenAI client with the API key and base URL

external_client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

set_default_openai_client(external_client)



agent = Agent(name="Assistant", instructions="Your name is Assistant. You are a helpful assistant.", model=MODEL)

result = Runner.run_sync(agent, "What is the capital of France?")

print(result.final_output)