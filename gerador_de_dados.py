import pandas as pd
import random
from datetime import datetime, timedelta
import os

os.makedirs("dados", exist_ok=True)

# Categorias empresariais
categorias_por_tipo = {
    "Receita": ["Venda Produto", "Venda Serviço", "Rendimento Investimento"],
    "Despesa": ["Aluguel", "Energia", "Marketing", "Manutenção", "Logística"],
    "Folha": ["Salário", "Encargos", "Benefícios"],
    "Imposto": ["IRPJ", "ISS", "ICMS", "INSS"],
    "Investimento": ["Compra Equipamento", "Sistema ERP", "Expansão Filial"],
}

centros_custo = ["Administrativo", "Vendas", "Financeiro", "TI", "Operações", "RH"]

clientes_fornecedores = [
    "Cliente Alfa", "Cliente Beta", "Cliente Gama", "Fornecedor XP", "Fornecedor YZ",
    "Banco Nacional", "Prestador Zeta", "Serviços Omega", "Fornecedor Global"
]

descricoes_extras = {
    "Receita": ["Venda realizada", "Serviço prestado", "Rendimento bancário"],
    "Despesa": ["Pagamento de conta", "Campanha Google Ads", "Frete logístico"],
    "Folha": ["Folha salarial", "Pagamento de benefícios"],
    "Imposto": ["Pagamento de tributo", "Retenção de imposto"],
    "Investimento": ["Compra de ativo", "Implementação sistema", "Obra física"]
}

def gerar_dados_empresariais(n=500):
    data_inicial = datetime(2023, 1, 1)
    registros = []

    for i in range(n):
        data = data_inicial + timedelta(days=random.randint(0, 500))
        tipo = random.choice(list(categorias_por_tipo.keys()))
        categoria = random.choice(categorias_por_tipo[tipo])
        descricao = random.choice(descricoes_extras[tipo])
        documento = f"NF-{random.randint(10000, 99999)}"
        cliente_forn = random.choice(clientes_fornecedores)
        centro = random.choice(centros_custo)

        # Valor depende do tipo
        if tipo == "Receita":
            valor = round(random.uniform(500, 15000), 2)
        elif tipo == "Investimento":
            valor = round(random.uniform(3000, 50000), 2) * -1
        elif tipo == "Folha":
            valor = round(random.uniform(1500, 8000), 2) * -1
        elif tipo == "Imposto":
            valor = round(random.uniform(500, 6000), 2) * -1
        else:  # Despesa
            valor = round(random.uniform(200, 10000), 2) * -1

        registros.append([
            data.date(), documento, descricao, tipo, categoria,
            valor, cliente_forn, centro
        ])

    df = pd.DataFrame(registros, columns=[
        "Data", "Documento", "Descrição", "Tipo", "Categoria",
        "Valor", "Cliente/Fornecedor", "Centro de Custo"
    ])

    df = df.sort_values(by="Data")
    df.to_csv("dados/lancamentos_empresariais.csv", index=False, sep=";")
    df.to_excel("dados/lancamentos_empresariais.xlsx", index=False)

    print("✅ Dados empresariais gerados com sucesso!")

if __name__ == "__main__":
    gerar_dados_empresariais()
