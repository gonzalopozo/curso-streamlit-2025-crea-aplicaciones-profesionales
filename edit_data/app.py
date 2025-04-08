import streamlit as st
import pandas as pd
import time

def main():
    st.header("Editor de datos")
    st.write("Sube tu archivo CSV para editar, guardar y descargar")

    csv_file = st.file_uploader('Subir archivo CSV', ['csv'])

    if csv_file:
        with st.form("formulario_edicion"):
            df = pd.read_csv (csv_file)
            modified_df = st.data_editor(df)
            save_modified_df = st.form_submit_button("¡Guardar datos!")

        if save_modified_df:
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            new_file_name = f"{csv_file.name.split('.')[0]}_{timestamp}.csv"

            final_df = modified_df.to_csv(index=False, encoding='utf-8')
            
            st.download_button(
                label='Descargar datos como CSV',
                data=final_df.encode('utf-8'),
                file_name=new_file_name,
                mime='text/csv'
            )

if __name__ == "__main__":
    main()