#%%
import pandas as pd

df = pd.DataFrame({
    'cliente': [1, 2, 3, 4, 5],
    'nome': ['Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo'],
})

df2 = pd.DataFrame({
    'cliente': [6, 7, 8],
    'nome': ['Fernanda', 'Gabriel', 'Helena'],
    'idade': [28, 34, 29],
})
#%%
df3 = pd.DataFrame({
    'idade': [40, 50, 60, 14, 32],
})
#%%
df
# %%
df2
# %%
df3
# %%
pd.concat([df, df3], axis=1) #concatenando na horizontal (esquerda para direita)
# %%
dfs = [df, df2]
pd.concat(dfs, ignore_index=True)
# %%
df3 = df3.sort_values(by='idade').reset_index(drop=True)
df3
# %%
pd.concat([df, df3], axis=1)
# %%
