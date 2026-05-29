import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def plotar_linha_temporal(df_plot, au_selecionada_grafico, emocao_selecionada, tipo_selecionado):
    """Gera gráfico de linha temporal"""

    fig_linha, ax_linha = plt.subplots(figsize=(10,4))
    sns.lineplot(data=df_plot, x='frame', y=au_selecionada_grafico, hue='dominio', ax=ax_linha)

    ax_linha.set_title(f"Evolução de Intensidade da {au_selecionada_grafico} ({emocao_selecionada} - {tipo_selecionado})")
    ax_linha.set_xlabel("Frames (Tempo)")
    ax_linha.set_ylabel("Intensidade (0 a 5)")

    return fig_linha

def plotar_diag_caixa(df_plot, au_selecionada_grafico, emocao_selecionada, tipo_selecionado):
    """Gera diagrama de caixa"""

    fig_box, ax_box = plt.subplots(figsize=(8,4))
    sns.boxplot(data=df_plot, x='dominio', y=au_selecionada_grafico, palette="Set2", ax=ax_box)

    ax_box.set_title(f"Dispersão da Variância da {au_selecionada_grafico} ({emocao_selecionada} - {tipo_selecionado})")
    ax_box.set_xlabel("Ambiente (Domínio)")
    ax_box.set_ylabel("Distribuição da Intensidade")

    return fig_box

def plotar_grafico_barra(df_planilha_final):
    """Gera gráfico de barra"""

    df_planilha_final['Suavizacao_Float'] = df_planilha_final['Suavização (%)'].str.replace('%', '').astype(float)
    df_ordenado = df_planilha_final.sort_values(by="Suavizacao_Float", ascending=False)

    fig_bar, ax_bar = plt.subplots(figsize=(12,5))
    sns.barplot(data=df_ordenado, x="Action Unit", y="Suavizacao_Float", palette="Reds_r", ax=ax_bar)

    ax_bar.set_title("Taxa de Perda de Intensidade por Músculo Facial")
    ax_bar.set_ylabel("Perda (%)")
    ax_bar.set_xlabel("Action Units")

    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    return fig_bar