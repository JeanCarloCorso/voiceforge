from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.tts_service import gerar_audio, listar_speakers

router = APIRouter(prefix="/tts", tags=["TTS"])

class TTSRequest(BaseModel):
    texto: str
    speaker: str

@router.get("/speakers")
def speakers():
    return listar_speakers()

@router.post("/generate")
def generate(req: TTSRequest):
    try:
        audio = gerar_audio(req.texto, req.speaker)
        return {"audio": audio}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
