import streamlit as st
from PIL import Image
import plotly.express as px
import pandas as pd
import time

favicon = Image.open("img/favicon.png")

st.set_page_config(page_title="Lebron's home", page_icon=favicon, layout="wide", initial_sidebar_state="collapsed")
# learn st.set_page_config sirve para modificar las configuraciones de la página
# learn page_title -> cambiar titulo
# learn page_icon -> cambiar favicon
# learn layout -> cambiar la estructura de la página, es decir como se mostrará la página
# learn initial_sidebar_state -> cambiar el estado inicial de la sidebar, la cual no aparecerá si no tiene contenido asignado en su interior

def test_spinner():
    st.title("Prueba de st.spinner()")
    st.write("Esta función simula una tarea en ejecución utilizando un spinner.")

    # learn Se muestra el spinner mientras se ejecuta una tarea simulada
    with st.spinner("¡Generando magia...!"):
        # learn Simula una tarea que toma 5 segundos
        time.sleep(5)

    # learn Muestra un mensaje de éxito una vez finalizada la tarea
    st.success("¡Tarea completada!")

def test_download_button():
    st.title("Prueba de st.download_button()")
    st.write("Haz clic en el botón para descargar el archivo '2023-2024-NBA-Player-Stats-Regular.xlsx'.")

    # Lee el archivo en modo binario
    try:
        with open("2023-2024-NBA-Player-Stats-Regular.xlsx", "rb") as file:
            file_data = file.read()
    except FileNotFoundError:
        st.error("El archivo no se encontró. Asegúrate de que '2023-2024-NBA-Player-Stats-Regular.xlsx' esté en el mismo directorio.")
        return

    # Botón de descarga
    st.download_button(
        label="Descargar archivo",
        data=file_data,
        file_name="datos_nba.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

def main():
    st.title("Welcome to Lebron's home")
    st.sidebar.header("Navegación") # learn La sidebar no aparecerá si no tiene contenido asignado en su interior

    df = pd.read_csv("NBA_Stats_2023-24_All_Stats_Playoffs.csv")
    st.dataframe(df)

    df_count = df.groupby('TEAM').count().reset_index()
    fig = px.pie(df_count, values="RANK", names="TEAM", title="Equipo") # learn Permite crear gráficos circulares de plotly
    st.plotly_chart(fig) # learn Muestra un gráfico de plotly

    df_count2 = df.groupby('POS').count().reset_index()
    fig2 = px.pie(df_count2, values="RANK", names="POS", title="Posiciones")
    st.plotly_chart(fig2)

    df_avg = df.groupby('POS')['MPG'].mean().reset_index()
    fig3 = px.bar(df_avg, x="POS", y="MPG", color="POS") # learn Permite crear gráficos de barras de plotly
    st.plotly_chart(fig3)

    test_spinner()
    test_download_button()

if __name__ == '__main__':
    main()