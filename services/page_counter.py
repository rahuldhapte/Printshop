import os
from PyPDF2 import PdfReader
from PIL import Image
from docx import Document


def count_pages(filepath):

    ext = filepath.split(".")[-1].lower()

    if ext == "pdf":
        reader = PdfReader(filepath)
        return len(reader.pages)

    elif ext in ["jpg", "jpeg", "png"]:
        return 1

    elif ext == "docx":
        doc = Document(filepath)
        paragraphs = len(doc.paragraphs)

        # rough estimate
        pages = max(1, paragraphs // 40)
        return pages

    else:
        return 1