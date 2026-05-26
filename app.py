import streamlit as st
import pandas as pd
import os

import src.data_loader as loader
from src.analysis import consolidar_analise

caminho_arquivo_geral = "data/processed/dataset_consolidado.csv"

if not os.path.exists(caminho_arquivo_geral):
    with st.spinner("Consolidando dados do OpenFace pela primeira vez"):
        loader.consolidar_tudo()
    st.success("Dados consolidados com sucesso!")

@st.cache_data
def carregar_dados():
    return pd.read_csv(caminho_arquivo_geral)

df_geral = carregar_dados()


st.title("Análise de Suavização de AUs (OpenFace)")

emocao_selecionada = st.selectbox("Escolha a Emoção:", ["Alegria", "Medo", "Nojo", "Raiva", "Surpresa", "Tristeza"])
au_selecionada = st.selectbox("Action Unit:", ["AU06_r", "AU12_r"])

resultados = consolidar_analise(df_geral, emocao_selecionada, "Micro", au_selecionada)

st.write("Resultados Estatísticos")
col1, col2, col3 = st.columns(3)

col1.metric("Mediana (Real)", f"{resultados['Real']['mediana']:.2f}")
col2.metric("Mediana (Virtual)", f"{resultados['Virtual']['mediana']:.2f}")
col3.metric("Taxa de Suavização", f"{resultados['Metricas_Comparativas']['Suavizacao_Percentual']:.1f}%")

st.write(f"**Correlação (O avatar imita bem?):** {resultados['Metricas_Comparativas']['Correlacao_Pearson']:.2f}")