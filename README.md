A simple web-based AI chatbot built with React (frontend) and FastAPI / Python (backend).
The chatbot answers professional questions using a small knowledge base. For unmatched questions, it can call the Google Gemini LLM if you provide an API key.

setup instructions 

1. git clone <github repo>
   - cd repo

2.cd frontend
   - npm install
   - npm run dev

3.cd backend
   - pip install fastapi uvicorn python-dotenv rapidfuzz google-generativeai
   - add your GEMINI_API_KEY to .env
   - uvicorn main:app --reload

Inorder to get the llm integrated answers , you have to create your gemini API Key and give your real api in .env.example and rename it as .env .
