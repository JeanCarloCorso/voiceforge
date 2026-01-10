import re

def preprocess_text(texto: str) -> str:
    texto = texto.strip()

    texto = texto.replace("...", "…")
    texto = re.sub(r"\.\s*", ".\n", texto)
    texto = re.sub(r"\?\s*", "?\n", texto)
    texto = re.sub(r"!\s*", "!\n", texto)
    texto = texto.replace(",", ", ")

    texto = re.sub(r"\n{3,}", "\n\n", texto)

    return texto
