# 🤖 IronLady AI Chatbot

[![Python](https://img.shields.io/badge/python-3.10+-blue?logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/streamlit-1.0-orange?logo=streamlit)](https://streamlit.io/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT-4o-mini-lightgrey?logo=openai)](https://openai.com/)

A smart, interactive AI chatbot that answers **FAQs about IronLady leadership programs** and can engage in casual conversation.

---

## 🌟 Features

- Real-time AI-powered responses using **OpenAI GPT-4o-mini**.  
- Pre-built **FAQ buttons** for common questions.  
- Free-text input for custom questions or casual chat.  
- **Auto-clearing input** after sending a message.  
- **Chat history saved** in session state.  
- Export chat history as **Markdown file** for reference or documentation.  
  

---

## ⚡ Quick FAQ Buttons

- What programs does IronLady offer?  
- Program duration?  
- Online or offline?  
- Certificates?  
- Mentors/coaches?  

---

## 🛠️ Tech Stack

- Python 3.10+  
- [Streamlit](https://streamlit.io/)  
- [OpenAI API](https://openai.com/)  
- GitHub for version control  

---

## 🚀 Installation & Run Locally

1. **Clone the repository:**
```bash
git clone https:/vidya-MLAI/github.com//ironlady-chatbot.git
cd ironlady-chatbot

**Create a virtual environment and activate**

python -m venv .venv
# Windows
.venv\Scripts\activate
# Mac/Linux
source .venv/bin/activate


**Install dependencies**

pip install -r requirements.txt

**Prepare database**

Make sure the faq_data.db (or your FAQ database file) is in the same directory.

Add your questions and answers if needed.

Running the App
streamlit run app.py


Open the URL shown in your terminal (usually http://localhost:8501).

Type your questions in the input box and press Enter or Submit.

The chatbot will respond based on stored FAQs or AI-generated answers (if enabled).

Create a virtual environment and activate

python -m venv .venv
# Windows
.venv\Scripts\activate
# Mac/Linux
source .venv/bin/activate


Install dependencies

pip install -r requirements.txt


Prepare database

Make sure the faq_data.db (or your FAQ database file) is in the same directory.

Add your questions and answers if needed.

Running the App
streamlit run app.py


Open the URL shown in your terminal (usually http://localhost:8501).

Type your questions in the input box and press Enter or Submit.

The chatbot will respond based on stored FAQs or AI-generated answers (if enabled).

**GUI Overview**

Input box: Enter your query.

Chat window: Displays conversation history.

Optional AI features: Can be added for dynamic answers.

**Notes**

Ensure Python 3.9+ is installed.

Database must be in place to answer FAQ questions.

Easily extendable to include AI-based recommendations or more interactive features.

Input box: Enter your query.

Chat window: Displays conversation history.

Optional AI features: Can be added for dynamic answers.



