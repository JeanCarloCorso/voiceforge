import re


def sanitize_for_tts(text: str) -> str:

    text = text.strip()

    text = re.sub(r"\s+([.,!?…])", r"\1", text)

    text = re.sub(r"\.{2,}", "…", text)

    if re.fullmatch(r"[.,!?…]+", text):
        return ""

    if len(text) < 2:
        return ""

    return text
