# %%
import pandas as pd

idades = [
    32, 38, 30, 30, 31, 
    35, 22, 20, 19, 20, 
    55, 17, 40, 30, 28
]

series_idades = pd.Series(idades)
series_idades
# %%
idades[0] #Primeiro elemento da lista
# %%
series_idades[-1] #Séries não são acessadas da mesma maneira que listas
# %%

#Reordenando a série com base nos valores de idade
series_idades = series_idades.sort_values()
series_idades

# %%
#Pega o indice com base na posição, e não pela chave
series_idades.iloc[-1]
# %%

# Pegando os três primeiro elementos da série reordenada
series_idades.iloc[:3]
# %%
series_idades.iloc[::-1] #Pega do último até o primeiro
# %%
idades = [
    32, 38, 30, 30, 31, 
    35, 22, 20, 19, 20, 
    55, 17, 40, 30, 28
]

indexs = [
    'Teo', 'Maria', 'Andreia', 'Matheus', 'Brendon',
    'Paula', 'Aline', 'Lucas', 'Paulo', 'Marcus',
    'Pedro', 'Eder', 'Deise', 'Maria Luísa', 'Lucas'
]

series_idades = pd.Series(idades, index=indexs)
series_idades
# %%
series_idades['Lucas'] #Dois index iguais com informações diferentes

# %%
print(series_idades.iloc[-1])
print(series_idades.loc['Teo'])
# %%
