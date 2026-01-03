#05.05 - Selecione a primeira transação diária de cada cliente.
#%%
import pandas as pd

transacoes = pd.read_csv('../../data/transacoes.csv', sep=';')
transacoes.head()


# %%
