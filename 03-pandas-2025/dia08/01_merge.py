#%%
import pandas as pd

transacoes = pd.read_csv('../data/transacoes.csv', sep=';')
transacoes.head()
# %%
clientes = pd.read_csv('../data/clientes.csv', sep=';')
clientes.head()
# %%
transacoes.head(
)
# %%
transacoes.merge(
    clientes,
    left_on=['IdCliente'],
    right_on=['idCliente'],
    how='left',
    suffixes=['Transacao', 'Cliente']
) #Left JOIN, estou indo na base de clientes a direita e buscando para transações a esquerda
# %%
#clientes.rename(columns={'idCliente': 'IdCliente'}, inplace=True)
