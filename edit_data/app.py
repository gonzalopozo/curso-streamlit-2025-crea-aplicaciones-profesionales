import streamlit as st
import pandas as pd

def main():
    st.header("Editor de datos")
    st.write("Sube tu archivo CSV para editar, guardar y descargar")

    csv_file = st.file_uploader('Subir archivo CSV', ['csv'])

    if csv_file:
        modified_csv_file = st.data_editor(pd.read_csv(csv_file))

        st.download_button(
            label='Descargatelo manin',
            data=modified_csv_file.to_csv(),
            file_name='datos_nba.csv',
            mime='text/csv'
        )

if __name__ == "__main__":
    main()