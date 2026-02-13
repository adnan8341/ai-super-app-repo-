from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from typing import Optional

# AI Libraries (Install these via requirements.txt)
import openai
import google.generativeai as genai

app = FastAPI()

# SECURITY: This allows your HTML file (on GitHub Pages) to talk to this server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, replace with your GitHub Pages URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str
    model: str

@app.post("/generate")
async def generate_response(request: ChatRequest):
    prompt = request.message
    model_choice = request.model.lower()

    try:
        if "gemini" in model_choice:
            genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content(prompt)
            return {"reply": response.text}

        elif "gpt" in model_choice or "openai" in model_choice:
            client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": prompt}]
            )
            return {"reply": response.choices[0].message.content}

        # Fallback for others (DeepSeek/Grok would follow similar logic)
        return {"reply": f"Model {model_choice} integrated but API key missing."}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
