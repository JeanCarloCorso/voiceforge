def get_voice_preset(emotion: str):
    presets = {
        "neutral": dict(
            speed=1.0,
            temperature=0.7,
            repetition_penalty=2.0,
            length_penalty=1.0
        ),
        "happy": dict(
            speed=1.05,
            temperature=0.85,
            repetition_penalty=1.8,
            length_penalty=0.95
        ),
        "sad": dict(
            speed=0.9,
            temperature=0.6,
            repetition_penalty=2.2,
            length_penalty=1.1
        ),
        "angry": dict(
            speed=1.1,
            temperature=0.9,
            repetition_penalty=2.5,
            length_penalty=0.9
        ),
        "anxious": dict(
            speed=1.0,
            temperature=0.8,
            repetition_penalty=2.3,
            length_penalty=1.05
        ),
        "calm": dict(
            speed=0.88,
            temperature=0.65,
            repetition_penalty=1.9,
            length_penalty=1.1
        )
    }

    return presets.get(emotion, presets["neutral"])
