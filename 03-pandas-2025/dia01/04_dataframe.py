# %%
import pandas as pd

idades = [
    32, 38, 30, 30, 31, 
    35, 22, 20, 19, 20, 
    55, 17, 40, 30, 28
]

nomes = [
    'Teo', 'Maria', 'Andreia', 'Matheus', 'Brendon',
    'Paula', 'Aline', 'Lucas', 'Paulo', 'Marcus',
    'Pedro', 'Eder', 'Deise', 'Maria Luísa', 'Lucas'
]

series_idades = pd.Series(idades)
series_nomes = pd.Series(nomes)

# %%
series_nomes
# %%
series_idades
# %%

df = pd.DataFrame()
df['idades'] = series_idades
df['nomes'] = series_nomes
df
# %%
df['nomes']
# %%
df.iloc[1] #Retorna uma série onde os índices serão as colunas do dataframe
# %%
df.iloc[0]['nomes']
# %%
df.iloc[-1]['idades'] #Idade da última pessoa do dataframe
# %%
