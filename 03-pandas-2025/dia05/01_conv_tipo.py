# %%
import pandas as pd

df = pd.read_csv('../data/clientes.csv', sep=';')
df
# %%

df['qtdePontos'].astype(float).astype(str) #conversão individual de um tipo de uma coluna

# %%
#Conversão de datas
replace = {
    '0000-00-00 00:00:00.000': '2025-11-11 22:50:00.000',
    '2025-10-01 00:00:00.000': '2025-11-11 22:50:00.000'
} #Substitui datas inválidas (para a biblioteca do pandas) por datas válidas

df['DtCriacao'] = pd.to_datetime(df['DtCriacao'].replace(replace))  # realiza a conversão
df['DtCriacao']
# %%
#Agora com a coluna convertida para data podemos acessar os seguintes recursos:
df['DtCriacao'].dt.year
df['DtCriacao'].dt.day
df['DtCriacao'].dt.month
df['DtCriacao'].dt.month_name()
df['DtCriacao'].dt.day_of_week
# %%
