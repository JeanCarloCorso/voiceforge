from typing import Optional
from TTS.api import TTS

class AppState:
    tts_model: Optional[TTS] = None

state = AppState()
