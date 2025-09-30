
import json
from rapidfuzz import process
from dotenv import load_dotenv
import os
import google.generativeai as GoogleGenerativeAI


load_dotenv()

gemini_key = os.getenv('GEMINI_API_KEY')
GoogleGenerativeAI.configure(api_key=gemini_key)



with open('./knowledge_base.json') as f:
    knowledge_base = json.load(f)




def get_answers(user_input :str) ->str:
   

    best_match,score,idx = process.extractOne(
        user_input , [q['question'] for q in knowledge_base]
    )
    

    if score >= 80:
        return knowledge_base[idx]['answer']
    else:
       if not gemini_key: 
           return 'No Gemini Api key found, only knowledge base questions will answered.'
       model = GoogleGenerativeAI.GenerativeModel("gemini-flash-lite-latest")
       chat = model.start_chat(history=[])

       response = chat.send_message(
        user_input,
        generation_config={
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 20, 
            "max_output_tokens": 90,
            }  
        ) 
       return response.text 
 
 
   