from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes import tts, speakers
from app.core.state import state
from TTS.api import TTS
from app.core.queue import start_worker
from app.core.config import OUTPUT_DIR
from fastapi.responses import FileResponse

app = FastAPI(title="VoiceForge")
app.mount("/audios", StaticFiles(directory=OUTPUT_DIR), name="audios")
app.mount("/frontend", StaticFiles(directory="app/frontend"), name="frontend")

@app.on_event("startup")
def load_tts_model():
    print("📥 Carregando modelo XTTS (apenas uma vez)...")
    state.tts_model = TTS(
        model_name="tts_models/multilingual/multi-dataset/xtts_v2",
        gpu=False
    )
    print("✅ Modelo XTTS carregado")

    print("🚀 Iniciando worker de geração de áudio...")
    start_worker()

app.include_router(tts.router)
app.include_router(speakers.router)

@app.get("/")
def home():
    return FileResponse("app/frontend/index.html")
