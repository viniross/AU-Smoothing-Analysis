import streamlit as st
import pandas as pd

AUS_DISPONIVEIS = [
    "AU01_r", "AU02_r", "AU04_r", "AU05_r", "AU06_r", "AU07_r", 
    "AU09_r", "AU10_r", "AU12_r", "AU14_r", "AU15_r", "AU17_r", 
    "AU20_r", "AU23_r", "AU25_r", "AU26_r", "AU45_r"
]

@st.cache_data
def carregar_dados_mestre():
    return pd.read_csv("data/processed/dataset_consolidado.csv")

def exibir_filtros_padrao():
    emocao = st.selectbox("Escolha a Emoção:", ["Alegria", "Medo", "Nojo", "Raiva", "Surpresa", "Tristeza"])
    tipo = st.selectbox("Selecione o Tipo", ["Micro", "Macro"])
    return emocao, tipo