import re

EMOTION_KEYWORDS = {
    "happy": ["feliz", "alegre", "ótimo", "maravilhoso", "excelente"],
    "sad": ["triste", "decepcionado", "infelizmente", "lamento"],
    "angry": ["raiva", "ódio", "irritado", "absurdo"],
    "anxious": ["nervoso", "ansioso", "preocupado", "medo"],
    "calm": ["tranquilo", "calmo", "sereno", "paz"]
}

def detect_emotion(text: str) -> str:
    text = text.lower()

    for emotion, keywords in EMOTION_KEYWORDS.items():
        for k in keywords:
            if re.search(rf"\b{k}\b", text):
                return emotion

    return "neutral"
