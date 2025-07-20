import chainlit as cl

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

agent3 = Agent(
    name = "Assistant",
    instructions = "You are an helpful assistant that is capable of helping with user queries"
)


@cl.on_chat_start
async def handle_chat_start():
    cl.user_session.set("history",[])
    await cl.Message(content="I am A Helpful Assistant Capable Of Helping Your Queries ! ").send()

@cl.on_message
async def main(message: cl.Message):
    history = cl.user_session.get("history")
    history.append({"role":"user","content":message.content})
    result3 = await Runner.run(
    agent3,
    input=history,
    run_config=config
    )
    history.append({"role":"assistant","content":result3.final_output})
    cl.user_session.set("history",history)
    await cl.Message(
        content=result3.final_output,
    ).send()