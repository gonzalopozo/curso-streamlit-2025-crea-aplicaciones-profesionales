import streamlit as st
from PIL import Image
import pandas as pd
import docx2txt
from PyPDF2 import PdfReader
import os

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

def save_file(uploaded_file):
    # Crear el directorio si no existe
    if not os.path.exists("temp"):
        os.makedirs("temp")

    # Guardar el archivo en el directorio
    with open(os.path.join("temp", uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())

    return st.success(f"Archivo guardado: {uploaded_file.name} en temp")

def main():
    st.title("Carga de archivos:")

    menu = ["Imágenes", "Conjunto de datos", "Archivos de documentos"]

    selectSidebar = st.sidebar.selectbox("Menú", menu)

    match selectSidebar:
        case "Imágenes":
            st.subheader("Imagen")
            img_file = st.file_uploader("Subir imagen", type=['png', 'jpg', 'jpeg'])


            if img_file: # La solución del profesor es 'if img_file is not None'
                file_details = {
                    "file_name": img_file.name,
                    "file_type": img_file.type,
                    "file_size": img_file.size,
                }

                st.write(file_details)

                st.write(load_image(img_file))

                save_file(img_file)


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

                save_file(data_file)

        case "Archivos de documentos":
            st.subheader("Archivos de documentos")

            document_file = st.file_uploader('Subir documento', type=["pdf", "docx", "txt"])
            
            if st.button("Procesar"):
                if document_file:
                    file_details = {
                        "file_name": document_file.name,
                        "file_type": document_file.type,
                        "file_size": document_file.size,
                    }

                    st.write(file_details)

                    text = None

                    match file_details["file_type"]:
                        case 'application/pdf':
                            text = read_pdf(document_file)

                        case 'text/plain':
                            text = str(document_file.read(), 'utf-8')
                            
                            # st.write(text)

                        case 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
                            # st.write('aaa')
                            text = docx2txt.process(document_file)

                    st.write(text)

                    save_file(document_file)

        case _:
            st.subheader("ERROR")

if __name__ == '__main__':
    main()