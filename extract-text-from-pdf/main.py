import os
import PyPDF2

def normalize_path(path):
    return os.path.normpath(path.strip('"'))

def extract_text_from_pdf(pdf_path, txt_path):
    with open(pdf_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfFileReader(pdf_file)
        with open(txt_path, 'w', encoding='utf-8') as txt_file:
            for page_num in range(reader.numPages):
                page = reader.getPage(page_num)
                text = page.extractText()
                txt_file.write(text)

if __name__ == "__main__":
    pdf_path = input("Enter the path to the PDF file: ")
    txt_path = input("Enter the path to save the text file: ")

    normalized_pdf_path = normalize_path(pdf_path)
    normalized_txt_path = normalize_path(txt_path)

    extract_text_from_pdf(normalized_pdf_path, normalized_txt_path)
    print(f"Text extracted and saved to {normalized_txt_path}")
