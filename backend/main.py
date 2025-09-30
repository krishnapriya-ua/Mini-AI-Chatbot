from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from chatbot import get_answers

app = FastAPI()

class Question(BaseModel):
    input:str

app.add_middleware(
    CORSMiddleware,
    allow_origins = ['http://localhost:5173'],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
) 


@app.post('/ask')
def askquestion(question:Question):
    answer = get_answers(question.input) 
    return{"answer":answer}
 