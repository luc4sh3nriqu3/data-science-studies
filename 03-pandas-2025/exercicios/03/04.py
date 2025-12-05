#%%
#03.04 - Qual o id do cliente no índice 4 no arquivo clientes.csv ?
import pandas as pd

clientes = pd.read_csv('../../data/clientes.csv', sep=';')
clientes.head()
# %%
print(f'Id do cliente no index 4: {clientes['idCliente'][4]}')
# %%
