import streamlit as st
import pandas as pd

df = pd.read_csv('NBA_Stats_2023-24_All_Stats_Playoffs.csv')

def main():
    # st.title("Curso de Streamlit") # Mostrar un h1
    # st.header("Esto es un encabezado") # Mostrar un h2
    # st.subheader("Esto es un sub encabezado") # Mostrar un h3
    # st.text("Hola, esto es un texto") # Mostrar un parrafo o un texto en un div
    # nombre  = "Gonzalo"
    # st.text(f"Hola {nombre}, esto es un texto") # Uso de variables dentro de strings usando f"string"
    # st.markdown("### Esto es markdown") # Tambien se puede usar la sintaxis de markdown

    # st.success("Éxito") # Mostrar un mensaje de exito
    # st.warning("Esto es una advertencia") # Mostrar un mensaje de advertencia
    # st.info("Esto es información") # Mostrar un mensaje informativo
    # st.error("Esto es un error") # Mostrar un mensaje de error
    # st.exception("Esto es una excepción") # Mostrar un mensaje de una excepción 

    # st.write("Texto normal") # st.write() acepta texto normal
    # st.write("## Esto es un teto de markdown") # st.write() también acepta texto markdown
    # st.write(1 + 2) # st.write() también acepta operaciones matematicas y casi puede mostrar cualquier cosa en la web
    # En general st.write() es el todoterreno a la hora de mostrar elementos usando streamlit

    # st.header("Dataframe:")
    # st.dataframe(df) # st.dataframe() muestra un dataframe como una tabla (por ejemplo, los dataframes de pandas como en este ejemplo)
    # # st.dataframe(df.style.highlight_max(axis=0)) # Destacar valores maximos de las columnas
    # # st.dataframe(df.head(100)) # Mostrar n filas desde el inicio
    # # st.dataframe(df.tail(100)) # Mostrar n filas desde el final

    # st.json({"clave": "valor"}) # Mostar un JSON

    # codigo = """
    #     const myName = "Gonzalo"
        
    #     function printName(name) {
    #         console.log(name)
    #     }

    #     printName(myName)
    #     """
    
    # st.code(codigo, language="js") # Mostrar un trozo de código definiendo el lenguaje para mostrar la sintaxis con colores

    st.title("Curso de Streamlit")

    # Selectbox
    option = st.selectbox( # Sirve para crear un select de HTML, la selección de este select se guardará en la variable con la cual creamos y asignamos el selectbox
        'Elige de qué posición quieres jugar 🏀',
        ['Base', 'Escolta', 'Alero', 'Ala-pívot', 'Pívot']
    )

    st.write(f"¡Vas a jugar de {option}!")

    options = st.multiselect(
        'Elige de qué posiciones puedes jugar 🏀',
        ['Base', 'Escolta', 'Alero', 'Ala-pívot', 'Pívot']
    )

    st.write(f"Puedes jugar de {', '.join(options)}!")

    ppg = st.slider(
        'Indica tu promedio de puntos por partido:',
        min_value=0.0, # Valor minimo
        max_value=40.0, # Valor maximo
        value=10.0, # Valor inicial
        step=0.1 # Valor por el cual se incrementara o decrementara al mover el slider
        # Todos los valores de los atributos deben ser del mismo tipo (int o float), pero no pueden ser unos int y otros float
    )

    st.write(f'Tus puntos por partido (ppg) son {ppg}')

if __name__ == "__main__":
    main()