import os
from app.core.config import OUTPUT_DIR
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.tts_service import gerar_audio, listar_speakers
from app.core.queue import task_queue
from uuid import uuid4
from app.core.task_store import tasks
from app.core.tasks import TTSTask

router = APIRouter(prefix="/tts", tags=["TTS"])

class TTSRequest(BaseModel):
    texto: str
    speaker: str

@router.get("/speakers")
def speakers():
    return listar_speakers()

@router.post("/generate")
def generate(req: TTSRequest):
    if req.speaker not in listar_speakers():
        raise HTTPException(status_code=400, detail="Speaker inválido")

    task_id = str(uuid4())

    task = TTSTask(
        id=task_id,
        texto=req.texto,
        speaker=req.speaker
    )

    tasks[task_id] = task
    task_queue.put(task_id)

    return {
        "task_id": task_id,
        "status": task.status
    }

@router.get("/status/{task_id}")
def status(task_id: str):
    task = tasks.get(task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Task não encontrada")

    return {
        "task_id": task.id,
        "status": task.status,
        "audio": task.audio_file,
        "error": task.error
    }

@router.get("/audios")
def listar_audios():
    return sorted(os.listdir(OUTPUT_DIR))