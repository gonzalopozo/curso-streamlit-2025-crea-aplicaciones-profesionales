import streamlit as st


def write_text():
    st.subheader("Sección de texto")
    st.write("Vamos a escribir un mensaje de éxito")
    st.success("Todo salió según lo esperado")

if __name__ == '__main__':
    write_text()