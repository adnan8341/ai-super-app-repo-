import os
import httpx
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="OmniAI Backend")

# SECURITY: Allow your GitHub Pages URL to access this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace ["*"] with your actual GitHub URL for better security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    model: str
    messages: List[Message]

@app.post("/generate")
async def generate_response(request: ChatRequest):
    # This key should be set in Render.com's Environment Variables
    api_key = os.getenv("OPENROUTER_API_KEY")
    
    if not api_key:
        raise HTTPException(status_code=500, detail="Backend API Key not configured")

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json",
                    "HTTP-Referer": "https://github.com/your-repo", # Optional: your site URL
                },
                json={
                    "model": request.model,
                    "messages": [m.dict() for m in request.messages]
                },
                timeout=60.0
            )
            
            if response.status_code != 200:
                raise HTTPException(status_code=response.status_code, detail=response.text)
                
            return response.json()
            
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def health_check():
    return {"status": "OmniAI Backend is Online"}
