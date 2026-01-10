VOICE_PRESETS = {
    "natural": {
        "speed": 0.92,
        "temperature": 0.7,
        "repetition_penalty": 2.1,
        "length_penalty": 1.05
    },
    "calmo": {
        "speed": 0.88,
        "temperature": 0.65,
        "repetition_penalty": 2.2,
        "length_penalty": 1.1
    },
    "emocional": {
        "speed": 1.0,
        "temperature": 0.8,
        "repetition_penalty": 1.9,
        "length_penalty": 1.0
    }
}

def get_voice_preset(mode: str):
    return VOICE_PRESETS.get(mode, VOICE_PRESETS["natural"])
