from dataclasses import dataclass
from typing import Optional

@dataclass
class TTSTask:
    id: str
    texto: str
    speaker: str
    status: str = "queued"
    audio_file: Optional[str] = None
    error: Optional[str] = None
