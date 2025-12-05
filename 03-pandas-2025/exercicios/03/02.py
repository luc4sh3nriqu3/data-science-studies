#%%
#03.02 - Quantas colunas do tipo int há no arquivo transacoes.csv ?
import pandas as pd
clientes = pd.read_csv('../../data/clientes.csv', sep=';')
clientes
# %%
int_columns = len(clientes.dtypes[clientes.dtypes == 'int64'].to_list())
print(f'Colunas do tipo inteiro: {int_columns}')
# %%
