#05.04 - Qual é o id de cliente que tem maior saldo de pontos? E o menor?
#%%
import pandas as pd

clientes = pd.read_csv('../../data/clientes.csv', sep=';')
clientes.head()

# %%
clientes = clientes.sort_values('qtdePontos', ascending=False)
clientes.head()
# %%
id_maior = clientes.iloc[0]['idCliente']
print(f'Id do cliente com maior saldo de pontos: {id_maior}')
# %%
