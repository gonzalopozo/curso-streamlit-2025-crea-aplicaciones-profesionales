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

def about_page():
    st.subheader("Acerca de ")

if __name__ == "__main__":
    main()