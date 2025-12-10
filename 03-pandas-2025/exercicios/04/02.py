#04.02 - Quantos clientes tem um saldo de pontos maior que 1000?
#%%
import pandas as pd
clientes = pd.read_csv('../../data/clientes.csv', sep=';')
clientes.head()
# %%
filtro = clientes['qtdePontos'] > 1000
print(f'Quantidade de clientes com saldo de pontos maior que 1000: {clientes[filtro].shape[0]}')
# %%
