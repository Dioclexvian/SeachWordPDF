import os
from pypdf import PdfReader

def search_for_text_in_pdf(file_path, text_to_search):
    pdf_reader = PdfReader(file_path)
    num_pages = len(pdf_reader.pages)

    for page_num in range(num_pages):
        page = pdf_reader.pages[page_num]
        text_in_page = page.extract_text()
        if text_to_search in text_in_page:
            return True

    return False


dir_path = 'dir/donde/están/losPdf'
text_to_search = 'Palabra a buscar'

for file_name in os.listdir(dir_path):
    if file_name.endswith('.pdf'):
        file_path = os.path.join(dir_path, file_name)
        found = search_for_text_in_pdf(file_path, text_to_search)

        if found:
            print(f'El texto "{text_to_search}" fue encontrado en el documento {file_name}.')
        else:
            print(f'El texto "{text_to_search}" no fue encontrado en el documento {file_name}.')