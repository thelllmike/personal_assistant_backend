from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import Engine
from transformers import AutoTokenizer, AutoModelForQuestionAnswering
import torch
import requests

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session  # Assuming you have these modules
# from .database import SessionLocal, engine

from bs4 import BeautifulSoup
from fastapi.middleware.cors import CORSMiddleware
from database import SessionLocal
from register import router as register_router

# Initialize the FastAPI app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your app's domain instead of "*"
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
     db = SessionLocal(bind=Engine)
     try:
         yield db
     finally:
         db.close()

app.include_router(register_router, prefix="/register", tags=["register"])
# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("bert-large-uncased-whole-word-masking-finetuned-squad")
model = AutoModelForQuestionAnswering.from_pretrained("bert-large-uncased-whole-word-masking-finetuned-squad")

class Question(BaseModel):
    question: str

def search_google(query):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    search_url = f"https://www.google.com/search?q={query}"
    response = requests.get(search_url, headers=headers)
    
    if response.status_code == 200:
        return response.text
    else:
        return None

def extract_snippet(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    snippet_div = soup.find('div', class_="BNeawe s3v9rd AP7Wnd")
    if snippet_div:
        return snippet_div.text
    else:
        return "Answer snippet not found."

@app.post("/ask")
async def answer_question(item: Question):
    html_content = search_google(item.question)
    if html_content:
        context = extract_snippet(html_content)
        if context == "Answer snippet not found.":
            return {"answer": "Failed to retrieve context from Google search results."}
    else:
        return {"answer": "Failed to retrieve answer."}
    
    inputs = tokenizer.encode_plus(item.question, context, add_special_tokens=True, return_tensors="pt")
    input_ids = inputs["input_ids"].tolist()[0]

    outputs = model(**inputs)
    answer_start_scores = outputs.start_logits
    answer_end_scores = outputs.end_logits

    answer_start = torch.argmax(answer_start_scores)
    answer_end = torch.argmax(answer_end_scores) + 1

    answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(input_ids[answer_start:answer_end]))
    return {"answer": answer}
