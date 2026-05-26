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