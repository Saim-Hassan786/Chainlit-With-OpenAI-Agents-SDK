import asyncio
GOOGLE_API_KEY = Place Your API Key Here

from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig

from openai.types.responses import ResponseTextDeltaEvent

external_client = AsyncOpenAI(
    api_key=GOOGLE_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-1.5-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

async def streaming():
    agent4=Agent(
        name="Assistant",
        instructions="You are a helpful assistant capable of helping the user with his queries"
    )
    run4 = Runner.run_streamed(
        agent4,
        "Tell me weird facts about pluto",
        run_config=config
    )
    async for event in run4.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            print(event.data.delta, end="", flush=True) 

asyncio.run(streaming())