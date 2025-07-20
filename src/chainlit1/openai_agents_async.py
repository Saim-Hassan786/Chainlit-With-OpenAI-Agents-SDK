import asyncio
GOOGLE_API_KEY = Place Your API Key Heresss

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

async def asynced():
    agent2=Agent(
        name="Assistant",
        instructions="You are a helpful assistant capable of helping the user with his queries"
    )
    run2 = await Runner.run(
        agent2,
        "Tell me weird facts about Mars",
        run_config=config
    )
    print("Agent Is called")
    print(run2.final_output)

asyncio.run(asynced())