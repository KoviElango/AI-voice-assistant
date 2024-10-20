from fastapi import FastAPI
from pydantic import BaseModel
import ollama

app = FastAPI()

class TextInput(BaseModel):
    prompt: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI backend!"}

@app.post("/process-text")
def process_text(input: TextInput):
    response = ollama.generate(model = "llama3.2:latest", prompt = input.prompt)
    return {"response": response.get('response')}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
