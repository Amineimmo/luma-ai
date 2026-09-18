import pymupdf as fitz

def extract_txt(pdf):
    doc = fitz.open(pdf)
    full_text = []
    for page in doc:
        text = page.get_text()
        full_text.append(text)
    return "\n".join(full_text)