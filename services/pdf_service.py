from PyPDF2 import PdfReader

def count_pdf_pages(filepath):
    reader = PdfReader(filepath)
    return len(reader.pages)