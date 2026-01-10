from datetime import datetime
import os
from app.core.config import SPEAKERS_DIR, OUTPUT_DIR
from app.core.state import state
from app.services.tts_pipeline import generate_tts_pipeline

def listar_speakers() -> list[str]:
    return [
        f for f in os.listdir(SPEAKERS_DIR)
        if f.lower().endswith(".wav")
    ]

def gerar_audio(texto: str, speaker: str) -> str:
    if not texto.strip():
        raise ValueError("Texto não pode ser vazio")

    if state.tts_model is None:
        raise RuntimeError("Modelo TTS não carregado")

    speaker_path = os.path.join(SPEAKERS_DIR, speaker)

    if not os.path.exists(speaker_path):
        raise FileNotFoundError("Speaker não encontrado")

    filename = generate_tts_pipeline(
        tts_model=state.tts_model,
        texto=texto,
        speaker_wav=speaker_path,
        output_dir=OUTPUT_DIR
    )

    return filename
