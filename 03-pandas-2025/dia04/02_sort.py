# %%
import pandas as pd

clientes = pd.read_csv('../data/clientes.csv', sep=';')
clientes
# %%
max_ponto = clientes['qtdePontos'].max() #Clientes que tem a maior quantidade de pontos
filtro = clientes['qtdePontos'] == max_ponto
clientes[filtro]
# %%
(clientes.sort_values(by='qtdePontos', ascending=False) #sort values retorna um dataframe novo
        .head(5)['idCliente']) #Retorna o ID dos 5 clientes que mais tem pontos
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
