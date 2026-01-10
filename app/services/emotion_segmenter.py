import re
from app.services.emotion_analyzer import detect_emotion

def split_by_emotion(text: str):
    sentences = re.split(r'(?<=[.!?])\s+', text)
    segments = []

    for s in sentences:
        emotion = detect_emotion(s)
        segments.append({
            "text": s.strip(),
            "emotion": emotion
        })

    return segments
