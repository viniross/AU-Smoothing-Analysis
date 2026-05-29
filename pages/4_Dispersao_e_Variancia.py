import streamlit as st
import pandas as pd

from src.analysis import consolidar_analise
from src.plots import plotar_diag_caixa
from src.utils import carregar_dados_mestre, exibir_filtros_padrao, AUS_DISPONIVEIS

st.title("Dispersão e Variância da Expressão")

df_geral = carregar_dados_mestre()

emocao_selecionada, tipo_selecionado = exibir_filtros_padrao()

au_selecionada_grafico = st.selectbox(
    "Escolha qual AU desenhar no gráfico:", 
    AUS_DISPONIVEIS
)

resultados_grafico = consolidar_analise(df_geral, emocao_selecionada, tipo_selecionado, au_selecionada_grafico)

df_real = resultados_grafico["Dados_Brutos"]["Real"]
df_cg = resultados_grafico["Dados_Brutos"]["Virtual"]
df_plot = pd.concat([df_real, df_cg])

figura_caixa = plotar_diag_caixa(df_plot, au_selecionada_grafico, emocao_selecionada, tipo_selecionado)
st.pyplot(figura_caixa)