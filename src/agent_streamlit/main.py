import os
import streamlit as st
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, set_default_openai_client, set_tracing_disabled

from dotenv import load_dotenv
import asyncio

load_dotenv()

st.title("ChatOrbit")
st.subheader("A versatile AI chatbot that lets you choose your brain — Gemini or Different models of Together AI — for smarter, faster answers.")

gemini_api_key = os.getenv("GEMINI_API_KEY")
aitogether_api_key = os.getenv("AI_TOGETHER_API_KEY")

external_provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

external_provider2 = AsyncOpenAI(
    api_key= aitogether_api_key,
    base_url="https://api.together.xyz/v1"
)

set_default_openai_client(external_provider)
set_tracing_disabled(True)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash", openai_client=external_provider
)
model1 = OpenAIChatCompletionsModel(
    model="deepseek-ai/DeepSeek-R1-Distill-Llama-70B", openai_client=external_provider2
)
model2 = OpenAIChatCompletionsModel(
    model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
    openai_client=external_provider2
)
model3 = OpenAIChatCompletionsModel(
    model="mistralai/Mixtral-8x7B-Instruct-v0.1",
    openai_client=external_provider2
)

with st.sidebar:
    model_selection = st.selectbox("Choose the model you wanna search with!",["Gemini 2.0 flash","Deep Seek R1", "Meta-Llama-3.1", "Mixtral-8x7B"])
    st.write("To clear chat history click Reset Chat!")
    if st.sidebar.button("Reset Chat"):
        st.session_state.chat_history = []

selected_model="Gemini 2.0 flash"

if model_selection=="Gemini 2.0 flash":
    selected_model=model
elif model_selection=="Deep Seek R1":
    selected_model=model1
elif model_selection=="Meta-Llama-3.1":
    selected_model=model2
elif model_selection=="Mixtral-8x7B":
    selected_model=model3


async def run_agent(agent, user_input):
    result = await Runner.run(agent, user_input)
    return result


def app():
    st.badge(label=model_selection,color="red")
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    agent = Agent(
        name="chatbot",
        instructions="Give the most suitable answer to the prompt given by user.",
        model=selected_model,
    )

    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    user_input = st.chat_input("Ask Anything")

    if user_input:
        with st.chat_message("user"):
            st.markdown(user_input)

        with st.spinner("Thinking..."):
            result = asyncio.run(run_agent(agent, user_input))

            if result:
                st.session_state.chat_history.append({"role": "User", "content": user_input})
                st.session_state.chat_history.append({"role": "Assistant", "content": result.final_output})

                with st.chat_message("assistant"):
                    st.markdown(result.final_output)

if __name__ == "__main__":
    app()