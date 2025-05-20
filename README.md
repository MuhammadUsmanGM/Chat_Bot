# 💬 ChatOrbit

**ChatOrbit** is a versatile and interactive AI chatbot built with **Streamlit**. It enables users to chat with various powerful large language models (LLMs) — including **Gemini 2.0**, **DeepSeek R1**, **Meta-LLaMA 3.1**, and **Mixtral-8x7B** — all from one clean interface. Choose your preferred model, ask anything, and get smart, fast answers.

---

## 🚀 Features

- 🧠 **Multi-Model Support**: Switch between Gemini and Together AI models seamlessly.
- 💬 **Chat History**: Preserves chat messages per session.
- 🔁 **Reset Chat**: Clear the conversation with a single click.
- 🎨 **Streamlit UI**: Clean, reactive UI built with Streamlit for simplicity and speed.
- ⚙️ **Async Execution**: Uses `asyncio` for efficient handling of AI requests.

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **Streamlit**
- **AsyncOpenAI wrapper**
- **Together AI & Gemini API**
- **Dotenv for API key management**

---

## 🔑 Requirements

Make sure you have the following API keys:

- `GEMINI_API_KEY` – for accessing Gemini models
- `AI_TOGETHER_API_KEY` – for accessing Together AI models

Create a `.env` file in the root directory:

`env
GEMINI_API_KEY=your_gemini_api_key
AI_TOGETHER_API_KEY=your_together_ai_key

🧪 Models Included
Model Name	Provider	Description
Gemini 2.0 Flash	Google Gemini	Fast, general-purpose model
DeepSeek R1	Together AI	LLaMA-based distillation
Meta-LLaMA 3.1 8B	Together AI	Instruction-tuned Meta model
Mixtral-8x7B Instruct	Together AI	Sparse mixture-of-experts model

🏷️ Topics
streamlit chatbot llm openai together-ai gemini-api python conversational-ai asyncio

📄 License
MIT License © 2025 [MuhammadUsmanGM]

🙌 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to change.
---

## 📸 Model Output Screenshots

### 🤖 Gemini 2.0 Output
![Gemini Output](Gemini%20Output.png)

### 🔍 DeepSeek R1 Output
![DeepSeek Output](DeepSeek%20Output.png)

### 🦙 Meta-LLaMA 3.1 Output
![Meta-Llama Output](Meta-Llama-3.1%20Output.png)

### 🔀 Mixtral-8x7B Output
![Mixtral Output](Mixtral7x8B%20Output.png)
