from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes import tts, speakers

app = FastAPI(title="VoiceForge")

app.include_router(tts.router)
app.include_router(speakers.router)

app.mount("/", StaticFiles(directory="static", html=True), name="static")
