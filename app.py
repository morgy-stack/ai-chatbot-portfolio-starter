import os
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

st.set_page_config(page_title="Business AI Assistant", page_icon="💬")
st.title("💬 Business AI Assistant")
st.caption("A portfolio demo: an AI chatbot that answers questions using a small business FAQ.")

FAQ_PATH = Path(__file__).parent / "sample_faq.md"
FAQ_TEXT = FAQ_PATH.read_text(encoding="utf-8") if FAQ_PATH.exists() else ""

SYSTEM_INSTRUCTIONS = f"""
You are a helpful customer-support assistant for the fictional business in the
provided FAQ. Answer using only the FAQ below.

Rules:
- If the FAQ does not contain the answer, say you don't have that information
  and suggest contacting the business.
- Never invent prices, policies, availability, contact details, or guarantees.
- Keep answers clear, friendly, and concise.
- Do not claim to have completed bookings, payments, refunds, or account changes.

BUSINESS FAQ:
{FAQ_TEXT}
"""

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.warning("Add your OpenAI API key to a local .env file to enable AI responses.")
    st.code("OPENAI_API_KEY=your_api_key_here", language="text")
    st.stop()

client = OpenAI(api_key=api_key)

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.subheader("Demo information")
    st.write("This assistant answers questions from the sample FAQ.")
    st.write("Try asking about services, opening hours, delivery, or returns.")
    if st.button("Clear conversation"):
        st.session_state.messages = []
        st.rerun()

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Ask the business assistant a question...")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = client.responses.create(
                    model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
                    instructions=SYSTEM_INSTRUCTIONS,
                    input=st.session_state.messages,
                )
                answer = response.output_text.strip()
                if not answer:
                    answer = "Sorry, I couldn't generate a response. Please try again."
            except Exception as exc:
                answer = (
                    "I couldn't reach the AI service. Please check the API key, "
                    "model setting, and network connection. "
                    f"Technical detail: {type(exc).__name__}"
                )
        st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})
