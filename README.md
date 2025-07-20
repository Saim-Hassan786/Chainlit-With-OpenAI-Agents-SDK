# 🧠 Chainlit + OpenAI Agent SDK Integration

This project demonstrates the integration of [Chainlit](https://www.chainlit.io/) with the [OpenAI Agents SDK](https://github.com/openai/openai-python/tree/main/src/openai/agents). It provides an interactive AI application where agents, tools, and workflows are structured and visualized via Chainlit's powerful frontend.


## 🎯 Purpose

The core idea is to **bridge agentic AI capabilities** with a **developer-friendly UI** using Chainlit. This allows for:

- Real-time interaction with multi-turn agents
- Visualization of streaming outputs and tool invocations
- Dynamic decision-making through OpenAI's Agent SDK
- Fine-grained tracing, debugging, and customization of agents

## 🧩 What Is Chainlit?

Chainlit is a Python-based UI framework designed for **LLM-powered apps**. It provides:

- Automatic session handling
- Rich message rendering (markdown, images, elements)
- Tool calling visualization
- Built-in support for async workflows


## 🔧 What Is OpenAI’s Agent SDK?

The Agent SDK by OpenAI is a modular framework for:

- Creating agent workflows with tools, memory, and goals
- Handling structured input/output with validation
- Streaming and tracing execution steps
- Running agent loops with decision-making

It abstracts and simplifies complex agent orchestration using:
- **Runners** for managing execution
- **Tools** with schema-based arguments
- **Schemas** for validating agent responses
- **Streaming** for real-time feedback

## ⚙️ Architecture Overview

User ⇄ Chainlit UI ⇄ Agent Runner ⇄ OpenAI Model & Tools

1. **Chainlit UI**: Captures user inputs and displays agent responses.
2. **Agent Runner**: Created using the OpenAI Agent SDK, defines the main workflow.
3. **Model**: Typically GPT-4 or another capable LLM.
4. **Tools**: Custom or built-in tools (e.g., search, math, APIs).
5. **Streaming**: Used to stream both the agent’s thought process and tool results.


## 🧠 Key Concepts

### 1. Agent
The agent is a goal-driven LLM process that can:
- Understand user queries
- Invoke tools
- Generate structured responses

### 2. Tool
A callable function exposed to the agent with:
- A defined schema
- Validation and error handling

### 3. Runner
An execution manager that:
- Orchestrates turns between user, model, and tools
- Can be `streamed` or `sync` based

### 4. Chainlit Integration
Chainlit manages:
- Lifecycle of the chat session
- Input/output display
- Live updates during agent streaming
- Buttons, forms, feedback, and visualization


## 🚀 Getting Started

Run with Chainlit:

```bash
chainlit run main.py -w
```


## 📌 Why Use This Setup?

* ✅ Modular, reusable agent structure
* ✅ Chainlit for fast frontend without React/HTML
* ✅ Streaming outputs for a better UX
* ✅ Clean tool integration with schema validation
* ✅ Ideal for teaching, tutoring, or assistant-like systems

---

## 📚 Learn More

* [OpenAI Agents SDK Docs](https://github.com/openai/openai-python/tree/main/src/openai/agents)
* [Chainlit Docs](https://docs.chainlit.io/)
* [OpenAI Function Calling](https://platform.openai.com/docs/guides/function-calling)

---

## 🧪 Sample Use Cases

* AI tutor or coach
* Customer support chatbot
* Research assistant
* Tool-augmented question answering
* Personal task manager

