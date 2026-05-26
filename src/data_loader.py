import os 
import pandas as pd

pasta_base = "data/raw"

subpastas = ["real_human", "virtual_human"]

lista_dataframes = []

for subpasta in subpastas:
    caminho_subpasta = os.path.join(pasta_base, subpasta)

    for nome_arquivo in os.listdir(caminho_subpasta):
        if nome_arquivo.endswith('.csv'):
            caminho_completo = os.path.join(caminho_subpasta, nome_arquivo)

            df_temp = pd.read_csv(caminho_completo)

            df_temp['arquivo_origem'] = nome_arquivo

            if subpasta == "real_human":
                df_temp['dominio'] = 'Real'
            else:
                df_temp['dominio'] = 'Virtual'

            lista_dataframes.append(df_temp)

df_geral = pd.concat(lista_dataframes, ignore_index=True)

df_geral.to_csv("data/processed/dataset_consolidado.csv", index=False)

print("Consolidação concluída com sucesso!")