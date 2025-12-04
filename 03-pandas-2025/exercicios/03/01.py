#%%
import pandas as pd

clientes = pd.read_csv('../../data/clientes.csv', sep=';')
clientes
# %%
print(f'Quantidade de linhas e colunas do dataframe: {clientes.shape}')
print(f'Quantidade apenas de linhas do dataframe: {clientes.shape[0]}')
print(f'Quantidade apenas de colunas do dataframe: {clientes.shape[1]}')
# %%
