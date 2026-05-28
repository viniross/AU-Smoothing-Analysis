import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

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
tipo_selecionado = st.selectbox("Selecione o Tipo", ["Micro", "Macro"])

linhas_da_planilha = []

aus_para_analisar = ["AU01_r", "AU02_r", "AU04_r", "AU05_r", "AU06_r", "AU07_r", "AU09_r", "AU10_r", "AU12_r", "AU14_r", "AU15_r", "AU17_r", "AU20_r", "AU23_r", "AU25_r", "AU26_r", "AU45_r"]

for au in aus_para_analisar:
    res = consolidar_analise(df_geral, emocao_selecionada, tipo_selecionado, au)

    linha = {
        "Action Unit": au,
        "Mediana Real": res["Real"]["mediana"],
        "Mediana Virtual": res["Virtual"]["mediana"],
        "Variância Real": res["Real"]["variancia"],
        "Variância Virtual": res["Virtual"]["variancia"],
        "Suavização (%)": f"{res['Metricas_Comparativas']['Suavizacao_Percentual']:.2f}%",
        "Correlação de Pearson": res["Metricas_Comparativas"]["Correlacao_Pearson"]
    }

    linhas_da_planilha.append(linha)

df_planilha_final = pd.DataFrame(linhas_da_planilha)

st.dataframe(df_planilha_final, use_container_width=True)

st.write("Dinâmica Temporal: Real vs Virtual")

au_selecionada_grafico = st.selectbox(
    "Escolha qual AU desenhar no gráfico: (Geralmente a com maior % na tabela acima)", 
    aus_para_analisar
)

resultados_grafico = consolidar_analise(df_geral, emocao_selecionada, tipo_selecionado, au_selecionada_grafico)

df_real = resultados_grafico["Dados_Brutos"]["Real"]
df_cg = resultados_grafico["Dados_Brutos"]["Virtual"]
df_plot = pd.concat([df_real, df_cg])

fig_linha, ax_linha = plt.subplots(figsize=(10,4))

sns.lineplot(data=df_plot, x='frame', y=au_selecionada_grafico, hue='dominio', ax=ax_linha)

ax_linha.set_title(f"Evolução de Intensidade da {au_selecionada_grafico} ({emocao_selecionada} - {tipo_selecionado})")
ax_linha.set_xlabel("Frames (Tempo)")
ax_linha.set_ylabel("Intensidade (0 a 5)")

st.pyplot(fig_linha)