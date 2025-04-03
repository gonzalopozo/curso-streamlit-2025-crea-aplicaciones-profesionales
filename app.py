import streamlit as st

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

    st.title("Curso de Streamlit")
    st.write("Texto normal") # st.write() acepta texto normal
    st.write("## Esto es un teto de markdown") # st.write() también acepta texto markdown
    st.write(1 + 2) # st.write() también acepta operaciones matematicas y casi puede mostrar cualquier cosa en la web
    # En general st.write() es el todoterreno a la hora de mostrar elementos usando streamlit


if __name__ == "__main__":
    main()