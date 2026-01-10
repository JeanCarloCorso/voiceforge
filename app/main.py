from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from app.routes import tts, speakers
from app.core.state import state
from TTS.api import TTS
from app.core.queue import start_worker
from app.core.config import OUTPUT_DIR
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates

app = FastAPI(title="VoiceForge")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/audios", StaticFiles(directory=OUTPUT_DIR), name="audios")
app.mount("/frontend", StaticFiles(directory="app/frontend"), name="frontend")

templates = Jinja2Templates(directory="app/frontend")

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


@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse(
        "pages/generate.html",
        {"request": request}
    )

@app.get("/speakers")
def speakers(request: Request):
    return templates.TemplateResponse(
        "pages/speakers.html",
        {"request": request}
    )

@app.get("/audios")
def audios(request: Request):
    return templates.TemplateResponse(
        "pages/audios.html",
        {"request": request}
    )

