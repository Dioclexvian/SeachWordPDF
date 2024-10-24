import os
import PyPDF2

def search_for_text_in_pdf(file_path, text_to_search):
    pdf_file_obj = open(file_path, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
    num_pages = pdf_reader.numPages

    for page_num in range(num_pages):
        page_obj = pdf_reader.getPage(page_num)
        text_in_page = page_obj.extract_text()
        if text_to_search in text_in_page:
            return True

    return False

# Uso de la función
dir_path = 'sourceFiles'
text_to_search = 'Moya Chaves'

for file_name in os.listdir(dir_path):
    if file_name.endswith('.pdf'):
        file_path = os.path.join(dir_path, file_name)
        found = search_for_text_in_pdf(file_path, text_to_search)

        if found:
            print(f'El texto "{text_to_search}" fue encontrado en el documento {file_name}.')
        else:
            print(f'El texto "{text_to_search}" no fue encontrado en el documento {file_name}.')