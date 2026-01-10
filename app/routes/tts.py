from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.tts_service import gerar_audio, listar_speakers
from app.core.queue import task_queue

router = APIRouter(prefix="/tts", tags=["TTS"])

class TTSRequest(BaseModel):
    texto: str
    speaker: str

@router.get("/speakers")
def speakers():
    return listar_speakers()

@router.post("/generate")
def generate(req: TTSRequest):
    task_queue.put({
        "texto": req.texto,
        "speaker": req.speaker
    })

    return {
        "status": "queued",
        "message": "Áudio adicionado à fila de geração"
    }
