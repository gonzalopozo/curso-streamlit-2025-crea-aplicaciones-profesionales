import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

@st.cache_data
def load_nba_file():
    nba_df = pd.read_parquet('./data/average.parq')
    print(nba_df.columns)
    print(nba_df.nunique())
    print(nba_df.dtypes)
    print(nba_df.head())
    return nba_df

# Configuración de la página 
st.set_page_config(
    page_title="Dashboard",
    page_icon="🤑",
    layout="wide"
)

st.title("🤑 Data visualization dashboard")
st.markdown('### Explorando diferentes bibliotecas de visualización en Python')

with st.expander("📄 Introducción", expanded=True):
    st.markdown("""
        Esta aplicación demuestra el uso de diferentes bibliotecas de visualización en Python:
        * **Matplotlib**: biblioteca base para visualización
        * **Seaborn**: visualizaciones estadísticas de alto nivel
        * **Plotly**: gráficos interactivos
        * **Streamlit**: framework para aplicaciones de datos
    """
    )

try:
    nba_df = load_nba_file()
    nba_df = nba_df.sort_values('PTS', ascending=False)

    st.success('✅ Datos cargados exitosamente')

    # Visualizaciones con Matplotlib
    st.header("🖌 Visualizaciones con Matplotlib")

    with st.container():
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Gráfico de dispersión")
            fig, ax = plt.subplots(figsize=(8, 6))
            players_names = nba_df['Player'].head(50)
            players_ppgs = nba_df['PTS'].head(50)
            ax.scatter(players_names, players_ppgs, color='blue', alpha=0.6)
            plt.xticks(rotation="vertical")
            plt.title('Mayores PPG de la historia de la NBA')
            plt.xlabel('Jugadores')
            plt.ylabel('PPG')
            st.pyplot(fig)
            plt.close()

        with col2:
            st.subheader("Gráfico de barras")
            fig, ax = plt.subplots(figsize=(8, 6))
            players_names = nba_df['Player'].head(50)
            players_ppgs = nba_df['PTS'].head(50)
            ax.bar(players_names, players_ppgs, color='skyblue')
            plt.xticks(rotation="vertical")
            plt.title('Mayores PPG de la historia de la NBA')
            plt.xlabel('Jugadores')
            plt.ylabel('PPG')
            st.pyplot(fig)
            plt.close()

    # Visualizaciones con Seaborn
    st.header("🎯 Visualizaciones con Seaborn")


    with st.container():
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Gráfico de violín")
            fig, ax = plt.subplots(figsize=(8, 6))
            sns.violinplot(data=nba_df, x='season', y='PTS')
            plt.xticks(rotation="vertical")
            plt.title('Mayores PPG de la historia de la NBA')
            st.pyplot(fig)
            plt.close()

        with col2:
            st.subheader("Gráfico de violín")
            fig, ax = plt.subplots(figsize=(8, 6))
            sns.boxplot(data=nba_df, x='season', y='PTS')
            plt.xticks(rotation="vertical")
            plt.title('Mayores PPG de la historia de la NBA')
            st.pyplot(fig)
            plt.close()
    



except Exception as e:
    st.error(f"❌ Error al cargar los datos: {str(e)}")
    st.error("Por favor, verifica que los archivos existan en la carpeta 'data' y tengan el formato correcto")