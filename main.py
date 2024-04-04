from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
import gemini

app = FastAPI()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

class Conversation(BaseModel):
    content: str

class Caution(BaseModel):
    content: str
    start_index: int
    end_index: int
    reason: str

class Result(BaseModel):
    result: List[Caution] = []

@app.get('/api/v1/desc')
async def get_desc():
    return gemini.get_desc()

@app.post("/api/v1/conv-analysis", response_model=Result)
async def get_caution(conversation: Conversation):
    return gemini.get_caution(conversation.content)
