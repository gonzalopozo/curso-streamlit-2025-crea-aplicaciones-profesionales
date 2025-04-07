import streamlit as st
import pandas as pd


def load_games():
    st.subheader("Aplicación de baloncesto")

    df = pd.read_csv("../NBA_Stats_2023-24_All_Stats_Playoffs.csv")

    st.dataframe(df)

if __name__ == '__main__':
    load_games()