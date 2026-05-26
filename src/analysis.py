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

