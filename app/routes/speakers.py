from fastapi import APIRouter, UploadFile, File, HTTPException
import os
from app.core.config import SPEAKERS_DIR

router = APIRouter(prefix="/speakers", tags=["Speakers"])

@router.post("/upload")
async def upload_speaker(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(".wav"):
        raise HTTPException(status_code=400, detail="Apenas arquivos WAV")

    path = os.path.join(SPEAKERS_DIR, file.filename)

    with open(path, "wb") as f:
        f.write(await file.read())

    return {"message": "Speaker enviado com sucesso"}
