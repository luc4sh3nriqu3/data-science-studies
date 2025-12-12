#05.02 - Aplique o log na coluna de saldo de pontos, criando uma coluna nova
#%%

import pandas as pd
from math import log

transacoes = pd.read_csv('../../data/transacoes.csv', sep=';')
transacoes.head()
# %%

#Usando apply
def transform_log(points):
    if points > 0:
        return round(log(points), 2)
    return 0

transacoes['logPoints'] = transacoes['QtdePontos'].apply(transform_log)
transacoes.head(n=20)
# %%
transacoes.dtypes
# %%
log(-1)
# %%
