# %%
import pandas as pd

df_clientes = pd.read_csv('../data/clientes.csv', sep=';')
df_clientes
# %%
# ================= AMOSTRAS =================
df_clientes.head(n=10) #Mostra o começo do dataset
# %%
df_clientes.tail(10) #Mostra o final do dataset

# %%
df_clientes.sample(10) #Pega 10 amostras aleatórias
# %%
df_clientes.shape #Atributo do dataframe que retorna uma tupla contendo as informações de linhas e colunas do dataframe
# %%
df_clientes.columns
# %%
df_clientes.index
# %%
df_clientes.info(memory_usage='deep')
# %%
df_clientes.dtypes #Série que mostra os valores da tipagem de cada campo/coluna do dataframe

# %%
df_clientes.dtypes['qtdePontos']
# %%
