import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfReader, PdfWriter


def select_file():
    root = tk.Tk()
    root.withdraw()  # Hide the Tkinter window
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        page_to_delete = int(input("Enter the page number to delete: "))
        delete_page(file_path, page_to_delete)


def delete_page(file_path, page_number):
    with open(file_path, 'rb') as pdf_file:
        pdf_reader = PdfReader(file_path)
        pdf_writer = PdfWriter()

        for page_num in range(len(pdf_reader.pages)):
            # Compare page numbers starting from 1
            if page_num + 1 != page_number:
                pdf_writer.add_page(pdf_reader.pages[page_num])

        with open('modified_file.pdf', 'wb') as output_file:
            pdf_writer.write(output_file)

    print("Page deleted successfully.")


if __name__ == "__main__":
    select_file()
