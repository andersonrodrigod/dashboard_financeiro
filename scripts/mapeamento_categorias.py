import pandas as pd
import os
from leitura_dados import carregar_dados

def filtrar_dados(df, filtros, valor=None, data_inicio=None, data_fim=None):
    for campo, valor in filtros.items():
        if isinstance(valor, list):
            df = df[df[campo].isin(valor)]
            print(f"🔍 Filtrando '{campo}' por múltiplos valores: {valor}")
        else:
            df = df[df[campo] == valor]
            print(f"🔍 Filtrando '{campo}' por valor único: {valor}")

    if data_inicio:
        df = df[df["Data"] >= pd.to_datetime(data_inicio)] 
        print(df["Data"].dtype) 

    if data_fim:
        df = df[df["Data"] <= pd.to_datetime(data_fim)]

    return df

    
caminho_arquivo = "dados/lancamentos_empresariais.csv"

df = carregar_dados(caminho_arquivo)

data_inicio = "2023-01-14"

filtros = {
    "Tipo": "Receita",
}

resultado = filtrar_dados(df, filtros, data_inicio)


print(resultado)