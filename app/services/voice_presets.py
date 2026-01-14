def get_voice_preset(emotion: str):
    presets = {
        "neutral": {
            "speed": 1.0,
        },
        "happy": {
            "speed": 1.08,
        },
        "sad": {
            "speed": 0.9,
        },
        "angry": {
            "speed": 1.12,
        },
        "anxious": {
            "speed": 1.05,
        },
        "calm": {
            "speed": 0.88,
        },
    }

    return presets.get(emotion, presets["neutral"])
