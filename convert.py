from docx import Document
from PyPDF2 import PdfReader

def pdf_to_docx(pdf_path, docx_path):
    reader = PdfReader(pdf_path)
    doc = Document()

    for page in reader.pages:
        text = page.extract_text()
        if text:
            doc.add_paragraph(text)
            doc.add_page_break()

    doc.save(docx_path)
    print(f"Файл сохранен: {docx_path}")


pdf_file = r"C:\Users\PC\PycharmProjects\run_test_demo\data\Тестовое задание.pdf"
docx_file = r"C:\Users\PC\PycharmProjects\run_test_demo\data\Тестовое задание.docx"


pdf_to_docx(pdf_file, docx_file)
