GOOGLE_API_KEY = Place Your API Key Heres
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig
import asyncio

from agents.tool import function_tool

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

@function_tool("weather_update")
def weather_info(location:str,unit:str="C"):
    """This tool is used to fetch The Weather Of the Given Location and Return the description given below"""
    return f"The Weather Is {location} is 25 {unit}"


async def tool():
    agent=Agent(
        name="Assistant",
        instructions = "You are a helpful assistant",
        tools=[weather_info],
        model = model
    )
    result = await Runner.run(
        agent,
        input="What is the weather in Lahore in fahrenheit"
    )
    print(result.final_output)

asyncio.run(tool())