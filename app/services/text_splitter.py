def split_text(text: str, max_len=180):
    lines = text.split("\n")
    chunks = []
    current = ""

    for line in lines:
        if len(current) + len(line) <= max_len:
            current += " " + line
        else:
            chunks.append(current.strip())
            current = line

    if current.strip():
        chunks.append(current.strip())

    return chunks
