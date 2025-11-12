# %%

import pandas as pd

df = pd.read_csv('../data/transacoes.csv', sep=';')
# %%
df
# %%
df.shape
# %%
df.info(memory_usage='deep')
# %%
df.dtypes
# %%
renamed_columns = {
    'QtdePontos': 'QtPontos',
    'DescSistemaOrigem': 'SistemaOrigem'
}
df.rename(columns=renamed_columns, inplace=True) #A chave do dicionário passado será o nome antigo e o valor será o nome novo
# %%
df[['IdCliente']] #Não retorna uma série, mas sim um dataframe com apenas uma coluna
# %%
df[['IdCliente', 'QtPontos']].sample(5)
# %%
# REORDENAR COLUNAS
colunas = list(df.columns)


# %%
colunas.sort()
# %%
df = df[colunas]
# %%
df
# %%
