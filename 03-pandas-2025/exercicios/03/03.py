#%%
#03.03 - Quantas colunas do tipo object há no arquivo produtos.csv ?
import pandas as pd

clientes = pd.read_csv('../../data/clientes.csv', sep=';')
clientes.head()
# %%
object_columns = len(clientes.dtypes[clientes.dtypes == 'object'].to_list())
print(f'Colunas do tipo object: {object_columns}')
# %%
clientes.dtypes
# %%
