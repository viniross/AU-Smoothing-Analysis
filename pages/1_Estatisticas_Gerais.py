import streamlit as st
import pandas as pd

from src.analysis import consolidar_analise
from src.analysis import calc_distorcao_absoluta_por_emocao
from src.plots import plotar_grafico_distorcao_emocao
from src.utils import carregar_dados_mestre, exibir_filtros_padrao, AUS_DISPONIVEIS

st.title("Tabela de Resultados Estatísticos")

df_geral = carregar_dados_mestre()

emocao_selecionada, tipo_selecionado = exibir_filtros_padrao() 

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

st.dataframe(df_planilha_final, use_container_width=True)

st.subheader("Análise Global: Qual emoção sofre mais distorção?")

# 1. Calcula a tabela com os dados
df_distorcao_emocoes = calc_distorcao_absoluta_por_emocao(df_geral, tipo_selecionado)

# 2. Gera o gráfico
figura_distorcao = plotar_grafico_distorcao_emocao(df_distorcao_emocoes, tipo_selecionado)

# 3. Mostra no ecrã
st.pyplot(figura_distorcao)