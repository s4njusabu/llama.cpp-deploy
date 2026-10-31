from fastapi import FastAPI
from dotenv import load_dotenv
import os, socket

load_dotenv()

app = FastAPI()

HOSTNAME = socket.gethostname()
MODEL_NAME = os.getenv("MODEL_NAME", "unknown")

@app.get("/")
def home():
    return {"llama.cpp model": MODEL_NAME, "version": "0.1.0", "hostname": HOSTNAME}
