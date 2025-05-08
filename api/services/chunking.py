import fitz  # PyMuPDF

async def extract_text_from_file(file):
    contents = await file.read()
    with fitz.open(stream=contents, filetype="pdf") as doc:
        text = "\n".join([page.get_text() for page in doc])
    return text

def chunk_text(text: str, max_length: int = 500) -> list:
    sentences = text.split(". ")
    chunks = []
    chunk = ""
    for sentence in sentences:
        if len(chunk) + len(sentence) < max_length:
            chunk += sentence + ". "
        else:
            chunks.append(chunk.strip())
            chunk = sentence + ". "
    if chunk:
        chunks.append(chunk.strip())
    return chunks
 