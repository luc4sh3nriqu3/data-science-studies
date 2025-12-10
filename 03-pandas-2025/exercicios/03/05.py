#%%
#03.05 - Qual o saldo de pontos do cliente na 10a posição (sem ordenar) do arquivo clientes.csv ?

import pandas as pd

clientes = pd.read_csv('../../data/clientes.csv', sep=';')
clientes.head(n=12)
# %%
saldo_10a_posicao = clientes['qtdePontos'].nlargest(10).iloc[-1] #cria um vetor com os 10 maiores valores e pega o último valor desse vetor
print(saldo_10a_posicao)

# %%
