import streamlit as st

def main():
    st.title("Mi apicación con session state")

    # Learn menu lateral
    menu = ['Home', 'Settings', 'About']
    choice = st.sidebar.selectbox("Menú", menu)

    if choice == "Home":
        home_page()
    elif choice == "Settings":
        settings_page()
    else:
        about_page()

def home_page():
    st.subheader("Página de inicio")
    if "contador" not in st.session_state:
        st.session_state.contador = 0

    def incrementar(): 
        st.session_state.contador += 1

    def decrementar(): 
        st.session_state.contador -= 1

    col1, col2 = st.columns(2)
    with col1:
        st.button("Incrementar", on_click=incrementar)

    with col2:
        st.button("Decrementar", on_click=decrementar)

    st.write(f"Valor del contador: {st.session_state.contador}")

def settings_page():
    st.subheader("Página de configuración")
    if "font_size" not in st.session_state:
        st.session_state.font_size = 20

    def incrementar(): 
        st.session_state.font_size += 1

    def decrementar(): 
        st.session_state.font_size -= 1

    col1, col2 = st.columns(2)
    with col1:
        st.button("Aumentar fuente", on_click=incrementar)

    with col2:
        st.button("Reducir fuente", on_click=decrementar)

    st.write(f"Tamaño de la fuente actual: {st.session_state.font_size}")

    st.html(f"""
        <p style="font-size: {st.session_state.font_size}px;">
            ¡MÍRAME!
        </p>
    """)


def about_page():
    st.subheader("Acerca de ")

if __name__ == "__main__":
    main()