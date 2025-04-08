import streamlit as st

def main():
    st.title("Tutorial de formularios en streamlit")

    menu = ["Inicio", "Formularios básicos", "Enfoques de formularios", "Reinicio de formularios"]
    sidebar_select_option = st.sidebar.selectbox("Selecciona una opción:", menu)

    match sidebar_select_option:
        case "Inicio":
            st.header("Bienvenido al tutorial de formularios en streamlit")
            st.write("""
            Este tutorial te enseñará sobre los formularios de Streamlit y sus diversas características:
            - Creación básica de formularios
            - Diferentes enfoques para crear formularios
            - Formularios con columnas (calculadora de salario)
            - Funcionalidad de reinicio de formularios
            """)

        case "Formularios básicos":
            st.header("Formularios básicos en streamlit")
            st.write("Aprenderemos cómo crear un formularios básico en streamlit")

            with st.form(key="formulario_basico"):
                st.write("Formulario simple de registro")
                name = st.text_input("Nombre:")
                lastname = st.text_input("Apellido:")
                submit_btn = st.form_submit_button(label="sign_up")

            if submit_btn:
                st.success(f"¡Hola {name} {lastname}! Has creado una cuenta")

        case "Enfoques de formularios":
            st.header("Dos enfoques para formularios")
            st.subheader("1. Enfoque como administrador de contexto")
            with st.form(key="formulario1"):
                st.write("Formulario 1 - Usando administrador de contexto")
                username = st.text_input("Nombre de usuario")
                submit_btn_form1 = st.form_submit_button(label="Iniciar sesión")

            if submit_btn_form1:
                st.success(f"¡Bienvenido {username}!")

        case "Reinicio de formularios":
            st.header("-------")

if __name__ == "__main__":
    main()