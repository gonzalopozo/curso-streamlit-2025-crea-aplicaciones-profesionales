import streamlit as st

def main():
    st.title("Tutorial de formularios en streamlit")

    menu = ["Inicio", "Formularios básicos", "Enfoques de formularios", "Calculadora de salario", "Reinicio de formularios"]
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
                submit_btn = st.form_submit_button(label="Iniciar sesión")

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

            st.subheader("2. Enfoque declarado")
            form2 = st.form(key="formulario2")
            form2.write("Formulario 2 - Usando enfoque declarado")
            job = form2.selectbox("Selecciona tu puesto de trabajo", ["Científico de datos", "Desarrollador WEB", "Contable"])
            submit_btn_form2 = form2.form_submit_button(label="Enviar")

            if submit_btn_form2:
                st.info(f"Tu puesto de trabajo es {job} 💪")

        case "Calculadora de salario":
            st.header("Formulario con columnas")

            with st.form(key="formulario_salario"):
                col1, col2, col3, col4 = st.columns(4)

                with col1:
                    hour_fee = st.number_input("Tarifa por hora en euros (€)", min_value=0.0)

                with col2:
                    hours_per_day = st.number_input("Horas cada día", min_value=0.30, max_value=8.30)

                with col3:
                    days_per_week = st.number_input("Días a la semana", min_value=1, max_value=7)

                with col4:
                    calcular = st.form_submit_button("Calcular salario")

                if calcular:
                    st.write("Prueba formularios con columnas")

        case "Reinicio de formularios":
            st.header("-------")

if __name__ == "__main__":
    main()