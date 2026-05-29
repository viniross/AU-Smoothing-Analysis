import pandas as pd
import numpy as np
import scipy.stats as stats

def separar_grupos(df_geral, emocao, tipo_expressao):
    """ 
    Filtra a tabela geral para a emoção e tipo escolhidos e 
    separa em dois DataFrames: Humano Real e Humano Virtual (CG).
    """

    df_filtrado = df_geral[(df_geral['Emocao'] == emocao) & (df_geral['Tipo'] == tipo_expressao)]

    df_real = df_filtrado[df_filtrado['dominio'] == 'Real']
    df_cg = df_filtrado[df_filtrado['dominio'] == 'Virtual']

    return df_real, df_cg

def calc_estatisticas_descritivas(df, coluna_au):
    """
    Calcula Mediana e Variância de uma Action Unit e retorna
    um dicionário com os resultados.
    """

    intensidades = df[coluna_au].dropna()

    if intensidades.empty:
        return {
            "mediana": 0.0,
            "variancia": 0.0,
            "maximo": 0.0
        }
    
    return {
        "mediana": intensidades.median(),
        "variancia": intensidades.var(),
        "maximo": intensidades.max()
    }

def calc_suavizacao(mediana_real, mediana_virtual):
    """
    Calcula a porcentagem de perda de intensidade (Suavização)
    quando a expressão foi transferida para o Avatar.
    """

    if mediana_real == 0:
        return 0.0
    
    perda = ((mediana_real - mediana_virtual) / mediana_real) * 100
    return perda

def calc_correlacao_temporal(df_real, df_cg, coluna_au):
    """
    Calcula a correlação de pearson frame a frame.
    "O movimento do avatar acompanhou o ritmo do humano?"
    """

    sinal_real = df_real[coluna_au].values
    sinal_cg = df_cg[coluna_au].values

    tam_min = min(len(sinal_real), len(sinal_cg))

    if tam_min < 2:
        return 0.0, 1.0 # 0 de correlacao e 1 de p-value
    
    sinal_real = sinal_real[:tam_min]
    sinal_cg = sinal_cg[:tam_min]

    correlacao, p_value = stats.pearsonr(sinal_real, sinal_cg)
    return correlacao

def exec_teste_estatistico(df_real, df_cg, coluna_au):
    """
    Aplica o Teste-T Independente para provar se a diferença de 
    intensidade entre Real e Avatar é estatisticamente significativa.
    """

    sinal_real = df_real[coluna_au].dropna()
    sinal_cg = df_cg[coluna_au].dropna()

    t_stat, p_value = stats.ttest_ind(sinal_real, sinal_cg, equal_var=False)

    significativo = p_value < 0.05

    return p_value, significativo

def obter_top_frames_aus(df_geral, emocao, tipo_expressao, dominio="Real", top_n_aus=5, top_n_frames=5):
    """
    Busca as AUs que atingiriam a maior força bruta e retorna 
    em quais frames exatos esses picos aconteceram.
    """

    df_video = df_geral[(df_geral['Emocao'] == emocao) &
                        (df_geral['Tipo'] == tipo_expressao) &
                        (df_geral['dominio'] == dominio)]
    
    if df_video.empty: 
        return pd.DataFrame()
    
    colunas_aus = [col for col in df_video.columns if col.startswith('AU') and col.endswith('_r')]

    maximos_por_au = df_video[colunas_aus].max()

    top_aus_nomes = maximos_por_au.nlargest(top_n_aus).index.tolist()

    lista_resultados = []

    for au in top_aus_nomes:
        top_linhas = df_video.nlargest(top_n_frames, au)

        for _, linha in top_linhas.iterrows():
            lista_resultados.append({
                "Action Unit": au,
                "Frame": int(linha['frame']),
                "Intensidade Bruta (0-5)": linha[au]
            })

    df_resultados = pd.DataFrame(lista_resultados)

    return df_resultados

def consolidar_analise(df_geral, emocao, tipo_expressao, coluna_au):
    """
    Executa todas funções acima e devolve um pacote 
    completo de métricas para o streamlit utilizar.
    """

    df_real, df_cg = separar_grupos(df_geral, emocao, tipo_expressao)

    stats_real = calc_estatisticas_descritivas(df_real, coluna_au)
    stats_cg = calc_estatisticas_descritivas(df_cg, coluna_au)

    suavizacao = calc_suavizacao(stats_real['mediana'], stats_cg['mediana'])
    correlacao = calc_correlacao_temporal(df_real, df_cg, coluna_au)
    p_value, significativo = exec_teste_estatistico(df_real, df_cg, coluna_au)

    return {
        "Real": stats_real,
        "Virtual": stats_cg,
        "Metricas_Comparativas": {
            "Suavizacao_Percentual": suavizacao,
            "Correlacao_Pearson": correlacao,
            "P_Value": p_value,
            "Diferenca_Significativa": significativo
        },
        "Dados_Brutos": {
            "Real": df_real,
            "Virtual": df_cg
        }
    }