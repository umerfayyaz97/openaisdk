from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig
import os
from dotenv import load_dotenv
load_dotenv()


#setting model and api key
# MODEL = "gemini/gemini-2.0-flash"
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

external_client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client,
)

config = RunConfig(
    model = model,
    model_provider=external_client,
    tracing_disabled = True,
)

agent = Agent(name="Assistant", instructions="Your name is Assistant. You are a helpful assistant.",)

result = Runner.run_sync(agent, "What is the capital of France?", run_config=config)

print(result.final_output)



