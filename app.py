import streamlit as st
import pandas as pd
from PIL import Image

df = pd.read_csv('NBA_Stats_2023-24_All_Stats_Playoffs.csv')

def main():
    # st.title("Curso de Streamlit") # learn Mostrar un h1
    # st.header("Esto es un encabezado") # learn Mostrar un h2
    # st.subheader("Esto es un sub encabezado") # learn Mostrar un h3
    # st.text("Hola, esto es un texto") # learn Mostrar un parrafo o un texto en un div
    # nombre  = "Gonzalo"
    # st.text(f"Hola {nombre}, esto es un texto") # learn Uso de variables dentro de strings usando f"string"
    # st.markdown("### Esto es markdown") # learn Tambien se puede usar la sintaxis de markdown

    # st.success("Éxito") # learn Mostrar un mensaje de exito
    # st.warning("Esto es una advertencia") # learn Mostrar un mensaje de advertencia
    # st.info("Esto es información") # learn Mostrar un mensaje informativo
    # st.error("Esto es un error") # learn Mostrar un mensaje de error
    # st.exception("Esto es una excepción") # learn Mostrar un mensaje de una excepción 

    # st.write("Texto normal") # learn st.write() acepta texto normal
    # st.write("## Esto es un teto de markdown") # learn st.write() también acepta texto markdown
    # st.write(1 + 2) # learn st.write() también acepta operaciones matematicas y casi puede mostrar cualquier cosa en la web
    # learn En general st.write() es el todoterreno a la hora de mostrar elementos usando streamlit

    # st.header("Dataframe:")
    # st.dataframe(df) # learn st.dataframe() muestra un dataframe como una tabla (por ejemplo, los dataframes de pandas como en este ejemplo)
    # # st.dataframe(df.style.highlight_max(axis=0)) # learn Destacar valores maximos de las columnas
    # # st.dataframe(df.head(100)) # learn Mostrar n filas desde el inicio
    # # st.dataframe(df.tail(100)) # learn Mostrar n filas desde el final

    # st.json({"clave": "valor"}) # learn Mostar un JSON

    # codigo = """
    #     const myName = "Gonzalo"
        
    #     function printName(name) {
    #         console.log(name)
    #     }

    #     printName(myName)
    #     """
    
    # st.code(codigo, language="js") # learn Mostrar un trozo de código definiendo el lenguaje para mostrar la sintaxis con colores

    # Selectbox
    # option = st.selectbox( # learn Sirve para crear un select de HTML, la selección de este select se guardará en la variable con la cual creamos y asignamos el selectbox
    #     'Elige de qué posición quieres jugar 🏀',
    #     ['Base', 'Escolta', 'Alero', 'Ala-pívot', 'Pívot']
    # )

    # st.write(f"¡Vas a jugar de {option}!")

    # options = st.multiselect(
    #     'Elige de qué posiciones puedes jugar 🏀',
    #     ['Base', 'Escolta', 'Alero', 'Ala-pívot', 'Pívot']
    # )

    # st.write(f"Puedes jugar de {', '.join(options)}!")

    # ppg = st.slider(
    #     'Indica tu promedio de puntos por partido:',
    #     min_value=0.0, # learn Valor minimo
    #     max_value=40.0, # learn Valor maximo
    #     value=10.0, # learn Valor inicial
    #     step=0.1 # learn Valor por el cual se incrementara o decrementara al mover el slider
    #     # Todos los valores de los atributos deben ser del mismo tipo (int o float), pero no pueden ser unos int y otros float
    # )

    # st.write(f'Tus puntos por partido (ppg) son {ppg}')

    # salary = st.select_slider(
    #     'Indica la franja en la que se encuentra tu salario:',
    #     ['500k-2.5M', '2.6M-12.5M', '12.6M-25.5M', '25.6M-37.5M', '37.6M-49.9M', '50M+'],
    #     value='12.6M-25.5M', # learn Valor inicial
    # )

    # st.write(f'Tu salario esta en la franja de {salary}')

    # imagen = st.select_slider(
    #     'Elige la foto de Lebron 🏀',
    #     options=['lebron1.jpg', 'lebron2.jpg', 'lebron3.jpg', 'lebron4.jpg'],
    #     value="lebron1.jpg", # Valor inicial
    # )

    # img = Image.open(f"img/{"".join(imagen)}")
    # st.image(img, use_container_width=True) # learn Muestra una imagen

    # with open("vid/lebron.mp4", "rb") as video_file:
    #     st.video(video_file.read(), start_time=0, loop=1, autoplay=1) # learn Muestra un video

    # with open('aud/lebron.mp3', 'rb') as audio_file:
    #     st.audio(audio_file.read())  # learn Muestra un audio

    st.title("Curso de Streamlit")

    name = st.text_input("Ingresa tu nombre:") # learn Muestra un input de texto de HTML
    description = st.text_area("Ingresa tu descripción:") # learn Muestra un textarea de HTML
    
    st.subheader(name)
    st.write(description)

    number = st.number_input("Ingresa tu número", min_value=1.0, max_value=30.0, step=0.5) # learn Muestra un input de número de HTML
    st.write(number) 

    date = st.date_input("Selecciona una fecha") # learn Muestra un input solo de fecha de HTML
    st.write(date)

    hour = st.time_input("Selecciona una hora", value="12:00:00") # learn Muestra un input solo de hora de HTML
    st.write(hour)

    color = st.color_picker("Selecciona un color") # learn Muestra un input de color de HTML, que devuelve el color en HEXADECIMAL como un string
    st.html( # learn Muestra código HTML
        f"""
        <div style="width:100px; height:100px; background-color:{color}; border-radius: 16px">
        </div>
        """
    )

if __name__ == "__main__":
    main()