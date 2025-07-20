GOOGLE_API_KEY = Place Your API Key Here

from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig

external_client = AsyncOpenAI(
    api_key=GOOGLE_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

agent1 : Agent = Agent(
    name="Assistant",
    instructions="You are an helpful Assistant",
    model=model
)

run1 = Runner.run_sync(
    agent1,
    "Hello! What is the meaning of Alpha Males",
    run_config= config
)

print("Calling Agent")
print(run1.final_output)


