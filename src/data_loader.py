import os 
import pandas as pd

def consolidar_tudo():
    pasta_base = "data/raw"
    subpastas = ["real_human", "virtual_human"]
    lista_dataframes = []

    for subpasta in subpastas:
        caminho_subpasta = os.path.join(pasta_base, subpasta)

        if not os.path.exists(caminho_subpasta):
            print(f"Pasta {caminho_subpasta} nao encontrada.")

        for nome_arquivo in os.listdir(caminho_subpasta):
            if nome_arquivo.endswith('.csv'):
                caminho_completo = os.path.join(caminho_subpasta, nome_arquivo)

                df_temp = pd.read_csv(caminho_completo)
                df_temp.columns = df_temp.columns.str.strip()

                df_temp['arquivo_origem'] = nome_arquivo

                if subpasta == "real_human":
                    df_temp['dominio'] = 'Real'
                else:
                    df_temp['dominio'] = 'Virtual'

                nome_min = nome_arquivo.lower()

                if "alegria" in nome_min or "happiness" in nome_min:
                    df_temp['Emocao'] = "Alegria"
                elif "raiva" in nome_min or "anger" in nome_min:
                    df_temp['Emocao'] = "Raiva"
                elif "surpresa" in nome_min or "surprise" in nome_min:
                    df_temp['Emocao'] = "Surpresa"
                elif "tristeza" in nome_min or "sadness" in nome_min:
                    df_temp['Emocao'] = "Tristeza"
                elif "medo" in nome_min or "fear" in nome_min:
                    df_temp['Emocao'] = "Medo"
                elif "nojo" in nome_min or "disgust" in nome_min:
                    df_temp['Emocao'] = "Nojo"
                else:
                    df_temp['Emocao'] = "Outra"
                
                if "micro" in nome_min:
                    df_temp['Tipo'] = "Micro"
                else:
                    df_temp['Tipo'] = "Macro"

                lista_dataframes.append(df_temp)

    if len(lista_dataframes) > 0:
        df_geral = pd.concat(lista_dataframes, ignore_index=True)
        os.makedirs("data/processed", exist_ok=True)
        df_geral.to_csv("data/processed/dataset_consolidado.csv", index=False)
        print("Consolidação concluída com sucesso! Colunas criadas.")
    else:
        print("Nenhum arquivo CSV foi encontrado nas pastas.")

if __name__ == "__main__":
    consolidar_tudo()