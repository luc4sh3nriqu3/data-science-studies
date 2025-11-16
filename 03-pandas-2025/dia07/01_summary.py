#%%
import pandas as pd

idades = [15, 22, 35, 45, 52, 63, 70, 80, 12, 33, 47, 58, 69, 74, 81]
idades = pd.Series(idades)

idades.sum() #Isso é uma agregação (reduz vários valores em um só)
idades.min() #Outra agregação
idades.max() #Outra agregação
idades.mean() #Outra agregação
idades.describe() #Retorna várias agregações de uma vez só
# %%
clientes = pd.read_csv('../data/clientes.csv', sep=';')
clientes
# %%
clientes['flTwitch'].sum()
clientes['flTwitch'].mean() #Média de clientes que usam Twitch
# %%
redes_sociais = ['flEmail', 'flTwitch', 'flYouTube', 'flBlueSky', 'flInstagram']
clientes[redes_sociais].mean()
# %%
filtro = clientes.dtypes == 'object' #Verificando quais colunas são do tipo object
# %%
clientes.dtypes[~filtro]
# %%
#Pegando apenas as colunas numéricas
num_colums = clientes.dtypes[~(clientes.dtypes == 'object')].index.tolist()
clientes[num_colums].mean()
# %%
clientes[num_colums].describe()
# %%
