import streamlit as st
from baloncesto import load_games
from texto import write_text

def main():
    st.title("Aplicación principal")

    menu = ["Inicio", "Baloncesto", "Texto","Conócenos"]

    choice = st.sidebar.selectbox("Menú", menu)

    match choice:
        case "Inicio":
            st.subheader("Inicio")

        case "Baloncesto":
            load_games()

        case "Texto":
            write_text()

        case "Conócenos":
            st.subheader("Conócenos")



if __name__ == '__main__':
    main()