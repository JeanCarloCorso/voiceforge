from datetime import datetime
import os
from TTS.api import TTS
from app.core.config import SPEAKERS_DIR, OUTPUT_DIR

print("📥 Carregando modelo XTTS (pode demorar)...")

tts = TTS(
    model_name="tts_models/multilingual/multi-dataset/xtts_v2",
    gpu=False
)

def listar_speakers() -> list[str]:
    return [
        f for f in os.listdir(SPEAKERS_DIR)
        if f.lower().endswith(".wav")
    ]

def gerar_audio(texto: str, speaker: str) -> str:
    if not texto.strip():
        raise ValueError("Texto não pode ser vazio")

    speaker_path = os.path.join(SPEAKERS_DIR, speaker)

    if not os.path.exists(speaker_path):
        raise FileNotFoundError("Speaker não encontrado")

    filename = f"audio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.wav"
    output_path = os.path.join(OUTPUT_DIR, filename)

    tts.tts_to_file(
        text=texto,
        speaker_wav=speaker_path,
        file_path=output_path,
        language="pt"
    )

    return filename
