import pandas as pd
import os
from leitura_dados import carregar_dados

def filtrar_dados(df, campo=None, valor=None, data_inicio=None, data_fim=None):
    if campo and valor:
        df = df[df[campo] == valor]
    if data_inicio:
        df = df[df["Data"] >= pd.to_datetime(data_inicio)]
    if data_fim:
        df = df[df["Data"] <= pd.to_datetime(data_fim)]
    return df

    
caminho_arquivo = "dados/lancamentos_empresariais.csv"

df = carregar_dados(caminho_arquivo)

campo = "Tipo"
valor = "Receita"

resultado = filtrar_dados(df, campo, valor)


print(resultado)