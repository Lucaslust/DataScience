# Instalação (se necessário): pip install kagglehub
import kagglehub
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Baixar a versão mais recente do dataset diretamente do Kaggle
path = kagglehub.dataset_download("kyanyoga/sample-sales-data")
print("Path to dataset files:", path)

# Caminho do arquivo CSV baixado localmente
caminho_arquivo = r"C:\Users\lucas\.cache\kagglehub\datasets\kyanyoga\sample-sales-data\versions\1\sales_data_sample.csv"

# Carregar o dataset no pandas
df = pd.read_csv(caminho_arquivo, encoding='latin1')

# Visualizar as 5 primeiras linhas do dataset
print(df.head())

# Verificar os nomes das colunas disponíveis
print(df.columns)

# Verificar tipos de dados e existência de valores nulos
print(df.info())

# --------------------------------------------
# ANÁLISE DE DADOS
# --------------------------------------------

# Total de vendas por país (ordenado do maior para o menor)
vendas_por_pais = df.groupby("COUNTRY")["SALES"].sum().sort_values(ascending=False)
print(vendas_por_pais)

# Gráfico de barras com total de vendas por país
vendas_por_pais.plot(kind="bar", figsize=(12, 6))
plt.title("Total de Vendas por País")
plt.ylabel("Vendas")
plt.xlabel("País")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Total de vendas por linha de produto (top 5)
vendas_produto = df.groupby("PRODUCTLINE")["SALES"].sum().sort_values(ascending=False)
print(vendas_produto.head(5))

# Converter a coluna de data para o tipo datetime
df["ORDERDATE"] = pd.to_datetime(df["ORDERDATE"])

# Criar colunas separadas para ano e mês
df["Ano"] = df["ORDERDATE"].dt.year
df["Mes"] = df["ORDERDATE"].dt.month

# Agrupar vendas por ano e mês
vendas_tempo = df.groupby(["Ano", "Mes"])["SALES"].sum()

# Gráfico de linha com evolução das vendas ao longo do tempo
vendas_tempo.plot(figsize=(12, 6))
plt.title("Vendas ao Longo do Tempo")
plt.ylabel("Vendas")
plt.xlabel("Ano/Mês")
plt.tight_layout()
plt.show()
