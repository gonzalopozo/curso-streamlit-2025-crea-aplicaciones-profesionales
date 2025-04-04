import streamlit as st
from PIL import Image

favicon = Image.open("img/favicon.png")

st.set_page_config(page_title="Lebron's home", page_icon=favicon, layout="wide")
# learn

def main():
    st.title("Welcome to Lebron's home")

if __name__ == '__main__':
    main()