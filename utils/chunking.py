def chunk_text(text, chunk_size=150, overlap=30):
    if overlap >= chunk_size:
        raise ValueError("Overlap must be smaller than chunk_size")

    if not text:
        return []

    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]

        if chunk.strip():
            chunks.append(chunk)

        start = end - overlap

    return chunks