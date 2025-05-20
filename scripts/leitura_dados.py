import pandas as pd
import os


def carregar_dados(caminho_arquivo):

    if not os.path.exists(caminho_arquivo):
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho_arquivo}")
    
    if caminho_arquivo.endswith(".csv"):
        df = pd.read_csv(caminho_arquivo, sep=";")
    elif caminho_arquivo.endswith(".xlsx"):
        df = pd.read_excel(caminho_arquivo)
    else:
        raise ValueError("Formato de arquivo inválido. Use .csv ou .xlsx")

    df["Data"] = pd.to_datetime(df["Data"], errors="coerce")
    df["Valor"] = pd.to_numeric(df["Valor"], errors="coerce")

    df = df.dropna(subset=["Data", "Valor"])

    df = df.sort_values(by="Data")

    return df























