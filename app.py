import os
import streamlit as st
from openai import OpenAI
from openai.types.chat import (
    ChatCompletion,
    ChatCompletionSystemMessageParam,
    ChatCompletionUserMessageParam,
    ChatCompletionAssistantMessageParam,
)
from datetime import datetime

# ----------------------------
# Page setup
# ----------------------------
st.set_page_config(page_title="IronLady Chatbot", page_icon="🤖", layout="wide")
st.title("🤖 IronLady AI Chatbot")
st.caption("Ask anything about IronLady programs or just chat casually.")

# ----------------------------
# API key (safe sharing)
# ----------------------------
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.info("No API key found in environment. Paste your own OpenAI API key to use the app.")
    api_key = st.text_input("🔑 OpenAI API Key", type="password", placeholder="sk-...")

if not api_key:
    st.stop()

client = OpenAI(api_key=api_key)

# ----------------------------
# Session state (chat history)
# ----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system",
         "content": (
             "You are a friendly, concise assistant who knows IronLady's leadership programs "
             "(offerings, duration, format, certificates, mentors) and can handle casual chat. "
             "If unsure, answer generally and suggest contacting IronLady for precise details."
         )}
    ]

# ----------------------------
# Sidebar: Quick FAQ buttons
# ----------------------------
st.sidebar.title("Quick Questions ❓")
faq_buttons = {
    "What programs does IronLady offer?": "What programs does IronLady offer?",
    "Program duration?": "What is the typical duration of the programs?",
    "Online or offline?": "Are the programs online or offline?",
    "Certificates?": "Are certificates provided?",
    "Mentors?": "Who are the mentors/coaches?"
}

for label, question in faq_buttons.items():
    if st.sidebar.button(label, key=label):
        st.session_state.send_faq = question  # only trigger sending, do NOT append here

# ----------------------------
# Sidebar: Download chat
# ----------------------------
def export_chat_md():
    md = "# Chat History with IronLady AI Chatbot\n\n"
    for export_msg in st.session_state.messages:
        if export_msg["role"] == "user":
            md += f"**You:** {export_msg['content']}\n\n"
        elif export_msg["role"] == "assistant":
            md += f"**Bot:** {export_msg['content']}\n\n"
    return md

st.sidebar.title("Export Chat 💾")
if st.sidebar.button("Download as Markdown"):
    chat_md = export_chat_md()
    filename = f"ironlady_chat_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    st.sidebar.download_button("Download", chat_md, file_name=filename, mime="text/markdown")

# ----------------------------
# Handle FAQ button trigger
# ----------------------------
user_text = st.chat_input("Type your message and press Enter")
if "send_faq" in st.session_state:
    user_text = st.session_state.send_faq
    del st.session_state["send_faq"]

# ----------------------------
# Render chat history
# ----------------------------
for chat_msg in st.session_state.messages:
    if chat_msg["role"] == "user":
        with st.chat_message("user"):
            st.markdown(chat_msg["content"])
    elif chat_msg["role"] == "assistant":
        with st.chat_message("assistant"):
            st.markdown(chat_msg["content"])

# ----------------------------
# Input (Enter to send + auto-clear)
# ----------------------------
if user_text:
    # 1) Add user message (works for typed input OR FAQ)
    st.session_state.messages.append({"role": "user", "content": user_text})
    with st.chat_message("user"):
        st.markdown(user_text)

    # 2) Convert to typed messages for OpenAI
    typed_messages: list[
        ChatCompletionSystemMessageParam
        | ChatCompletionUserMessageParam
        | ChatCompletionAssistantMessageParam
    ] = []
    for typed_msg in st.session_state.messages:
        role = typed_msg["role"]
        if role == "system":
            typed_messages.append(ChatCompletionSystemMessageParam(role="system", content=typed_msg["content"]))
        elif role == "user":
            typed_messages.append(ChatCompletionUserMessageParam(role="user", content=typed_msg["content"]))
        elif role == "assistant":
            typed_messages.append(ChatCompletionAssistantMessageParam(role="assistant", content=typed_msg["content"]))

    # 3) Get AI response
    try:
        response: ChatCompletion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=typed_messages,
            temperature=0.6,
            max_tokens=400,
        )
        reply = response.choices[0].message.content or "Sorry, I couldn’t generate a response."
    except Exception as e:
        reply = f"⚠️ Error: {e}"

    # 4) Save & display bot reply
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)
