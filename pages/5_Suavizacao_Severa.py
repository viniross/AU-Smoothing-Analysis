import streamlit as st
import pandas as pd

from src.analysis import consolidar_analise
from src.plots import plotar_grafico_barra
from src.utils import carregar_dados_mestre, exibir_filtros_padrao, AUS_DISPONIVEIS

st.header("Onde a suavização é mais severa?")

df_geral = carregar_dados_mestre()

emocao_selecionada, tipo_selecionado = exibir_filtros_padrao()

au_selecionada_grafico = st.selectbox(
    "Escolha qual AU desenhar no gráfico:", 
    AUS_DISPONIVEIS
)

linhas_da_planilha = []

for au in AUS_DISPONIVEIS:
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

figura_barra = plotar_grafico_barra(df_planilha_final)
st.pyplot(figura_barra)