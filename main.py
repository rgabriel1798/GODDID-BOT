from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")  # Tu clave en variable de entorno

app = FastAPI()

# Configuración CORS - permitir todas las conexiones (puedes limitar después)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambia "*" por tu dominio en producción si quieres
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Question(BaseModel):
    message: str

@app.post("/chat")
async def chat_endpoint(q: Question):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": q.message}]
    )
    answer = response.choices[0].message.content
    return {"response": answer}
