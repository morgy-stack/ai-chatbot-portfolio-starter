# Business AI Assistant — Portfolio Demo

A small Streamlit chatbot that answers customer questions using a fictional business FAQ and the OpenAI API.

## Features
- Chat-style web interface
- FAQ-grounded responses
- Clear fallback when the FAQ does not contain an answer
- Conversation history during the current session
- No real orders, payments, refunds, or customer accounts are accessed

## Requirements
- Python 3.10+
- An OpenAI API key with API access enabled

## Run locally

1. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   ```

   Windows PowerShell:

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

   macOS/Linux:

   ```bash
   source .venv/bin/activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Copy `.env.example` to `.env` and add your API key:

   ```env
   OPENAI_API_KEY=your_real_key
   OPENAI_MODEL=gpt-4.1-mini
   ```

   Keep `.env` private. Never commit it to GitHub or share it with clients.

4. Start the app:

   ```bash
   streamlit run app.py
   ```

## Test questions
- What are your opening hours?
- How long does standard shipping take?
- Can I return an unused item?
- Can you tell me where my order is?

The final question should receive a limitation/fallback response because the demo has no order-system access.

## Customization
Replace the fictional content in `sample_faq.md` with approved client FAQ content. For a real client project, agree on data privacy, hosting, API costs, escalation behavior, and integration scope before deployment.

## Portfolio description
**Business AI Assistant:** Built a Streamlit chatbot using the OpenAI API. The assistant answers customer questions from a business FAQ, follows grounding instructions, and avoids inventing unsupported policy or order information.

## Current limitations
- Uses a small static FAQ included with the project
- No retrieval database or document upload interface
- No user authentication or persistent chat storage
- No live order lookup, booking, payment, or CRM integrations
- Requires an API key and may incur API usage charges
