import random


def enhance_text(text: str, emotion: str) -> str:

    text = text.strip()

    if emotion == "sad":
        text = text.replace(".", "…")
        text = text.replace("!", "…")
        text = slow_connectors(text)

    elif emotion == "angry":
        text = text.replace(".", "!")
        text = emphasize_words(text)

    elif emotion == "happy":
        text = text.replace(".", "!")
        text = lighten_text(text)

    elif emotion == "calm":
        text = text.replace(",", ", ")
        text = soften_text(text)

    return text


def emphasize_words(text: str) -> str:
    words = text.split()
    if len(words) > 4:
        idx = random.randint(1, len(words) - 2)
        words[idx] = f"{words[idx].upper()}"
    return " ".join(words)


def slow_connectors(text: str) -> str:
    for c in ["porque", "mas", "então", "porém"]:
        text = text.replace(f" {c} ", f"… {c} … ")
    return text


def lighten_text(text: str) -> str:
    return text.replace("!", "! ")


def soften_text(text: str) -> str:
    return text.replace(".", ". ")
