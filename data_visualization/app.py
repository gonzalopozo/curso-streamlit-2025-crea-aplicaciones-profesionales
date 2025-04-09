import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

@st.cache_data
def load_nba_file():
    nba_df = pd.read_parquet('./data/average.parq')
    nba_df.reset_index(inplace=True)
    return nba_df

@st.cache_data
def load_nba_playoffs_file():
    nba_playoffs_df = pd.read_parquet('./data/average_playoffs.parq')
    nba_playoffs_df.reset_index(inplace=True)
    return nba_playoffs_df

# learn Configuración de la página 
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

    # learn Visualizaciones con Matplotlib
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

    # learn Visualizaciones con Seaborn
    st.header("🎯 Visualizaciones con Seaborn")


    with st.container():
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Gráfico de violín")
            fig, ax = plt.subplots(figsize=(8, 6))
            sns.violinplot(data=nba_df, x='season', y='PTS')
            plt.xticks(rotation="vertical")
            plt.title('PPG por temporada de la historia de la NBA')
            st.pyplot(fig)
            plt.close()

        with col2:
            st.subheader("Gráfico de violín")
            fig, ax = plt.subplots(figsize=(8, 6))
            sns.boxplot(data=nba_df, x='season', y='PTS')
            plt.xticks(rotation="vertical")
            plt.title('PPG por temporada de la historia de la NBA')
            st.pyplot(fig)
            plt.close()
    
    # learn Visualizaciones interactivas con Plotly
    st.header("🎩 Visualizaciones interactivas con Plotly")

    with st.container():
        # learn Gráficos de línea interactivo
        nba_df = nba_df.sort_values('index')


        kobe_df = nba_df[nba_df['Player'] == 'Kobe Bryant']
        fig = px.line(
            kobe_df,
            x='season',
            y='PTS',
            title='PPG por temporada de Kobe Bryant',
            markers=True,
        )

        st.plotly_chart(fig, use_container_width=True)

        # learn 1. Sumar los partidos jugados por jugador
        grouped_df = nba_df.groupby('Player')['G'].sum().reset_index()

        # learn 2. Filtrar jugadores con al menos 100 partidos
        players_100 = grouped_df[grouped_df['G'] >= 100]['Player']

        # learn 3. Filtrar el DataFrame original con solo esos jugadores
        filtered_df = nba_df[nba_df['Player'].isin(players_100)]

        # learn 4. Agrupar por edad y sacar promedio de puntos
        ages_df = filtered_df.groupby('Age')['PTS'].mean().reset_index()

        # learn 5. Pie chart con Plotly
        fig2 = px.pie(
            ages_df,
            names='Age',
            values='PTS',
            title='Promedio de PTS por Edad (jugadores con ≥ 100 partidos)',
            hole=0.3
        )  # learn Puedes quitar hole si no quieres donut

        st.plotly_chart(fig2, use_container_width=True)

    # learn Sección interactiva
    st.header("🧠 Sección interactiva")

    # learn Selector dataset
    dataset_choice = st.radio(
        "Selecciona el conjunto de datos",
        ["Temporada regular", "Playoffs"]
    )

    if dataset_choice == "Temporada regular":
        df = load_nba_file()
    else:
        df = load_nba_playoffs_file()

    graph_type = st.selectbox(
        'Selecciona el tipo de gráfico',
        ['Barras','Dispersión', 'Línea']
    )

    x = st.selectbox('Selecciona el eje X', df.columns)
    y = st.selectbox('Selecciona el eje Y', df.columns)

    if graph_type == "Barras":
        fig3 = px.bar(df, x=x, y=y)
    elif graph_type == "Dispersión":
        fig3 = px.scatter(df, x=x, y=y)
    else:
        fig3 = px.line(df, x=x, y=y)

    st.plotly_chart(fig3, use_container_width=True)



except Exception as e:
    st.error(f"❌ Error al cargar los datos: {str(e)}")
    st.error("Por favor, verifica que los archivos existan en la carpeta 'data' y tengan el formato correcto")