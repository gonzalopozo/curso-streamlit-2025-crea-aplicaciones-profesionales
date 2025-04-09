import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

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