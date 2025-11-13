#%%
import pandas as pd

clientes = pd.read_csv('../data/clientes.csv', sep=';')
clientes
# %%
#05.05 - Selecione a primeira transação diária de cada cliente.

transacoes = pd.read_csv('../data/transacoes.csv', sep=';')
transacoes
# %%
transacoes['data'] = pd.to_datetime(transacoes['DtCriacao']).dt.date
transacoes = transacoes.sort_values('DtCriacao')

first = transacoes.drop_duplicates(keep='first', subset=['IdCliente', 'data'])
first
# %%
last = transacoes.drop_duplicates(keep='last', subset=['IdCliente', 'data'])
last
# %%
