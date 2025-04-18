🎯 Job Application Assistant — Goal-Oriented AI Agent

Welcome to the Job Application Assistant! This is an interactive Streamlit web app powered by LangChain, Google Gemini 2.0, and PDF parsing tools. It acts as a smart, goal-based conversational agent to help users complete a job application by collecting three essential pieces of information:

🧑 Name

📧 Email

🛠️ Skills

✨ Features

🧠 Conversational AI Agent

Uses LangChain’s CHAT_CONVERSATIONAL_REACT_DESCRIPTION agent type

Retains context using ConversationBufferMemory

Driven by Gemini 2.0 Flash from Google Generative AI

📄 Resume Parsing (Optional)

Upload your resume (PDF or TXT)

Automatically extract name, email, and skills using PyMuPDF and regex

✅ Goal Tracker

Continuously monitors application completion

Informs users of missing fields

Notifies when the application is ready to download

💬 Chat Interface

Sleek and friendly chat UI with emojis and avatars

Interactive chat with persistent memory

📥 Export Summary

Download your completed application summary as a text file

Install Dependencies

Set Up Environment Variables

Create a .env file in the root directory and add your Gemini API key:

GEMINI_API_KEY=your_google_generative_ai_key

Run the App

streamlit run app.py

🧪 Sample Usage

Type “Hi, my name is Hira Khalid” and watch the assistant extract your name.

Say “My email is hira@example.com.”

Share your skills: “I know Python, React, and Machine Learning.”

Optionally, upload your resume to auto-fill this info.

🛠️ Tech Stack

Streamlit – Web UI

LangChain – Agent + Tools

GoogleGenerativeAI – LLM (Gemini 2.0)

PyMuPDF (fitz) – PDF parsing

Python’s re – Regex-based info extraction

dotenv – Environment variable loader

👩‍💻 Developed By

Hira Jabeen — AI Enthusiast & Applied GenAI Learner
📚 PIAIC | GIAIC
💡 Motto: “The ones who try never fail.”

📬 Contact:
📧 Email: your-email@example.com
🌐 LinkedIn: your-linkedin
🐦 Twitter: @yourhandle

📝 License

MIT License — Free to use and modify. Credit appreciated!
