import fitz  # PyMuPDF
from bs4 import BeautifulSoup
import sys, glob, os

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)
        text += page.get_text()
    return text



def extract_text_from_html(html_path):
    with open(html_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
    return soup.get_text()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        pdf_dir_input = sys.argv[1]
        html_dir_input = sys.argv[2]
    else:
        print("debes pasar como argumento el path a un directorio con archivos pdf y despues otro con archivos html")
    
    pdf_files = glob.glob(os.path.join(pdf_dir_input, "*.pdf"))
    html_files = glob.glob(os.path.join(html_dir_input,"*.html"))
    pdf_txts = ""
    html_txts = ""
    for path_pdf in pdf_files:
        pdf_txts += extract_text_from_pdf(path_pdf)
    for path_html in html_files:
        html_txts += extract_text_from_html(path_html)
    print(pdf_txts)
    print(html_txts)