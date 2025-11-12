# %%
import pandas as pd

clientes = pd.read_csv('../data/clientes.csv', sep=';')
clientes
# %%
max_ponto = clientes['qtdePontos'].max() #Clientes que tem a maior quantidade de pontos
filtro = clientes['qtdePontos'] == max_ponto
clientes[filtro]
# %%
top_5 = (clientes.sort_values(by='qtdePontos', ascending=False) #sort values retorna um dataframe novo
        .head(5)['idCliente']) #Retorna o ID dos 5 clientes que mais tem pontos

type(top_5)
# %%
brinquedo = pd.DataFrame(
    {
        'nome': ['lucas', 'matheus', 'pedro', 'malu'],
        'idade': [22, 17, 3, 16],
        'salario': [2500, 1800, 670, 1800]
    }
)
brinquedo
# %%
brinquedo.sort_values(by=['salario', 'idade'], ascending=[False, True]) #Colocando dois critérios de ordenação (1°: salario - decrescente; 2°: idade - crescente )
# %%
