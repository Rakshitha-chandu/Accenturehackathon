
import fitz  # PyMuPDF

def parse_resume(path):
    text = ""
    with fitz.open(path) as doc:
        for page in doc:
            text += page.get_text()
    return text
