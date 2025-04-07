import streamlit as st
from PIL import Image
import pandas as pd
import docx2txt
from PyPDF2 import PdfReader

@st.cache_data
def load_image(image_file):
    img = Image.open(image_file)
    return img

def read_pdf(pdf_file):
    pdfReader = PdfReader(pdf_file)
    count = len(pdfReader.pages)
    all_the_text = ""

    for i in range(count):
        page = pdfReader.pages[i]
        all_the_text += page.extract_text()
    
    return all_the_text

def main():
    st.title("Carga de archivos:")

    menu = ["Imágenes", "Conjunto de datos", "Archivos de documentos"]

    selectSidebar = st.sidebar.selectbox("Menú", menu)

    match selectSidebar:
        case "Imágenes":
            st.subheader("Imágenes")
            img_file = st.file_uploader("Subir imágen", type=['png', 'jpg', 'jpeg'])

        case "Conjunto de datos":
            st.subheader("Conjunto de datos")

        case "Archivos de documentos":
            st.subheader("Archivos de documentos")

        case _:
            st.subheader("ERROR")

if __name__ == '__main__':
    main()