import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

import src.data_loader as loader
from src.analysis import consolidar_analise
from src.analysis import obter_top_frames_aus

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

st.header("Tabela de Resultados Estatísticos")

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

st.header("Inspeção de Picos Máximos (Frames)")

dominio_pico = st.radio("Qual ambiente inspecionar?", ["Real", "Virtual"])

df_picos = obter_top_frames_aus(df_geral, emocao_selecionada, tipo_selecionado, dominio=dominio_pico)

if not df_picos.empty:
    st.dataframe(df_picos, use_container_width=True)
else:
    st.warning("Nenhum dado encontrado para essa combinação.")

st.header("Dinâmica Temporal: Real vs Virtual")

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

st.header("Dispersão e Variância da Expressão")

fig_box, ax_box = plt.subplots(figsize=(8,4))

sns.boxplot(data=df_plot, x='dominio', y=au_selecionada_grafico, palette="Set2", ax=ax_box)

ax_box.set_title(f"Evolução de Intensidade da {au_selecionada_grafico} ({emocao_selecionada} - {tipo_selecionado})")
ax_box.set_xlabel("Ambiente (Domínio)")
ax_box.set_ylabel("Distribuição da Intensidade")

st.pyplot(fig_box)

st.header("Onde a suavização é mais severa?")

df_planilha_final['Suavizacao_Float'] = df_planilha_final['Suavização (%)'].str.replace('%', '').astype(float)

df_ordenado = df_planilha_final.sort_values(by="Suavizacao_Float", ascending=False)

fig_bar, ax_bar = plt.subplots(figsize=(12,5))

sns.barplot(data=df_ordenado, x="Action Unit", y="Suavizacao_Float", palette="Reds_r", ax=ax_bar)

ax_bar.set_title("Taxa de Perda de Intensidade por Músculo Facial")
ax_bar.set_ylabel("Perda (%)")
ax_bar.set_xlabel("Action Units")

plt.xticks(rotation=45, ha='right')
plt.tight_layout()

st.pyplot(fig_bar)