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
            st.subheader("ImAGEN")
            img_file = st.file_uploader("Subir imágen", type=['png', 'jpg', 'jpeg'])


            if img_file: # La solución del profesor es 'if img_file is not None'
                file_details = {
                    "file_name": img_file.name,
                    "file_type": img_file.type,
                    "file_size": img_file.size,
                }

                st.write(file_details)

                st.write(load_image(img_file))

        case "Conjunto de datos":
            st.subheader("Conjunto de datos")

            data_file = st.file_uploader("Subir CSV o excel", type=['csv', 'xlsx'])

            if data_file: # La solución del profesor es 'if data_file is not None'
                file_details = {
                    "file_name": data_file.name,
                    "file_type": data_file.type,
                    "file_size": data_file.size,
                }

                st.write(file_details)

                df = None 

                if file_details["file_type"] == 'text/csv':
                    df = pd.read_csv(data_file)
                    # st.write('hola')

                elif file_details["file_type"] == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
                    df = pd.read_excel(data_file)

                st.dataframe(df)

        case "Archivos de documentos":
            st.subheader("Archivos de documentos")

        case _:
            st.subheader("ERROR")

if __name__ == '__main__':
    main()