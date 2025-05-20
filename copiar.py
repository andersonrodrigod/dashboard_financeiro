import pandas as pd
import os

def carregar_dados(caminho_arquivo):
    """
    Lê o arquivo de lançamentos (CSV ou Excel) e retorna um DataFrame limpo.
    """
    if not os.path.exists(caminho_arquivo):
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho_arquivo}")

    # Detecta extensão do arquivo
    if caminho_arquivo.endswith(".csv"):
        df = pd.read_csv(caminho_arquivo, sep=";")
    elif caminho_arquivo.endswith(".xlsx"):
        df = pd.read_excel(caminho_arquivo)
    else:
        raise ValueError("Formato de arquivo inválido. Use .csv ou .xlsx")

    # Conversão de tipos
    df["Data"] = pd.to_datetime(df["Data"], errors="coerce")
    df["Valor"] = pd.to_numeric(df["Valor"], errors="coerce")

    # Remover registros com data ou valor inválido
    df = df.dropna(subset=["Data", "Valor"])

    # Ordenar por data
    df = df.sort_values(by="Data")

    return df
