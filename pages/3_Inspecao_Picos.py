import streamlit as st

from src.analysis import obter_top_frames_aus
from src.utils import carregar_dados_mestre, exibir_filtros_padrao, AUS_DISPONIVEIS

st.title("Inspeção de Picos Máximos (Frames)")

df_geral = carregar_dados_mestre()

emocao_selecionada, tipo_selecionado = exibir_filtros_padrao()

dominio_pico = st.radio("Qual ambiente inspecionar?", ["Real", "Virtual"])

df_picos = obter_top_frames_aus(df_geral, emocao_selecionada, tipo_selecionado, dominio=dominio_pico)

if not df_picos.empty:
    st.dataframe(df_picos, use_container_width=True)
else:
    st.warning("Nenhum dado encontrado para essa combinação.")