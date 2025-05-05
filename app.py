import os
import gradio as gr
from groq import Groq

# Load your API key from environment variables (do NOT hardcode it!)
API_KEY = os.environ.get("GROQ_API_KEY")

# Initialize Groq client
client = Groq(api_key=API_KEY)

# Chat function
def chatbot(message, history=[]):
    try:
        messages = [{"role": "system", "content": "You are a helpful assistant."}]
        for user_msg, bot_msg in history:
            messages.append({"role": "user", "content": user_msg})
            messages.append({"role": "assistant", "content": bot_msg})
        messages.append({"role": "user", "content": message})

        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=messages,
        )

        reply = response.choices[0].message.content
        return reply

    except Exception as e:
        return f"[ERROR] {str(e)}"

# Gradio Interface
chat_interface = gr.ChatInterface(
    fn=chatbot,
    title="Grok Chatbot",
    description="A chatbot using Groq's LLaMA 3 model",
)

# Launch the Gradio app
if __name__ == "__main__":
    chat_interface.launch()
