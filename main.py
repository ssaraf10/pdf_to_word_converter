from pathlib import Path
import PyPDF2
from docx import Document


def pdf_to_text(pdf_path):
    text = ''
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

def text_to_docx(text, docx_path):
    document = Document()
    document.add_paragraph(text)
    document.save(docx_path)

def main():
    folder_path = Path(r"C:\Users\sweth\OneDrive\Shashank\Shashank EB1B\Shashank manuscript")
    for file_path in folder_path.rglob("*.pdf"):
        print(file_path)

    for file_path in folder_path.rglob("*.pdf"):
        print(file_path)
        pdf_path = file_path.as_posix()
        file_name = file_path.name[:-4] + "_output.docx"
        docx_path = file_path.parent / file_name

        text = pdf_to_text(pdf_path)
        text_to_docx(text, docx_path)

if __name__ == "__main__":
    main()
