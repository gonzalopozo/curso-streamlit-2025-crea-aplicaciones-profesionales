import streamlit as st
from PIL import Image
import pandas as pd
import docx2txt
from PyPDF2 import PdfReader

@st.cache_data
def load_image(image_file):
    img = Image.open(image_file)
    return img

def leer_pdf(pdf_file):
    pdfReader = PdfReader(pdf_file)
    count = len(pdfReader.pages)
    all_the_text = ""

    for i in range(count):
        page = pdfReader.pages[i]
        all_the_text += page.extract_text()
    
    return all_the_text
