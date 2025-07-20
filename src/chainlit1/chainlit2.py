import chainlit as cl

GOOGLE_API_KEY = Place Your API Key Here

from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig
from openai.types.responses import ResponseTextDeltaEvent


external_client = AsyncOpenAI(
    api_key=GOOGLE_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-1.5-pro",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

agent= Agent(
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
    msg = cl.Message(content = "")
    await msg.send()
    result = Runner.run_streamed(
    agent,
    input=history,
    run_config=config
    )
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            await msg.stream_token(event.data.delta)
    history.append({"role":"assistant","content":result.final_output})
    cl.user_session.set("history",history)
    # await cl.Message(
    #     content=result.final_output,
    # ).send()