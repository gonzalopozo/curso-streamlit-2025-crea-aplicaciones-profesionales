import streamlit as st
from PIL import Image
import plotly.express as px
import pandas as pd

favicon = Image.open("img/favicon.png")

st.set_page_config(page_title="Lebron's home", page_icon=favicon, layout="wide", initial_sidebar_state="collapsed")
# learn st.set_page_config sirve para modificar las configuraciones de la página
# learn page_title -> cambiar titulo
# learn page_icon -> cambiar favicon
# learn layout -> cambiar la estructura de la página, es decir como se mostrará la página
# learn initial_sidebar_state -> cambiar el estado inicial de la sidebar, la cual no aparecerá si no tiene contenido asignado en su interior

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

if __name__ == '__main__':
    main()