# %%
idades = [
    32, 38, 30, 30, 31, 
    35, 22, 20, 19, 20, 
    55, 17, 40, 30, 28
]

media = sum(idades) / len(idades)
print(f'Média = {media}')

diffs = 0
for i in idades:
    diffs += (i - media) ** 2

variancia = diffs / (len(idades) - 1)
print(f'Variância = {variancia}')
# %%
import pandas as pd

# %%
#Criando uma série (a partir da lista de idades criada)
series_idades = pd.Series(idades)
series_idades
# %%

#Métodos do objeto Series:
media_idades = series_idades.mean()
var_idades = series_idades.var()
summary_idades = series_idades.describe()
summary_idades
# %%
