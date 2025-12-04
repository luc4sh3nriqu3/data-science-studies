#%%
import pandas as pd

transacoes = pd.read_csv('../../data/transacoes.csv', sep=';')
transacoes.head()
# %%
transacoes['valores_1'] = 1
print(f'Quantidade de valores de cada linha somados: {transacoes['valores_1'].sum()}')
transacoes
# %%
transacoes.to_csv('transacoes_1.csv', index=False)
# %%
