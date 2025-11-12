# %%
import pandas as pd

clientes = pd.read_csv('../data/clientes.csv', sep=';')

clientes
# %%
clientes.dropna() #Remove todas as linhas que tenham ao menos um NaN
# %%
clientes.dropna(how='all') #Retira apenas dados em que a linha inteira é composta por NaN
clientes.dropna(how='any') #Remove todas as linhas que tenham ao menos um NaN


# %%
df = pd.DataFrame(
    {
        'nome': ['lucas', None, 'matheus', 'pedro', 'malu'],
        'idade': [None, None, 17, 3, 16],
        'salario': [2500, 1800, 670, None, 1890]
    }
)

df.dropna() #Permanecerão apenas as linhas 2 e 4
df.dropna(how='all') #Não removerá nenhuma, pois nenhuma linha é inteira NaN
df.dropna(how='all', subset=['idade']) #Remove apenas linhas em que a idade é NaN
df.dropna(how='all', subset=['idade', 'salario']) #Remove as linhas em que TODOS os dados dentro do subset sejam NaN (nesse caso idade e salário)
df.dropna(how='any', subset=['idade', 'salario']) #Remove as linhas em que AO MENOS UM dos dados dentro do subset seja NaN (idade e salário)
df.dropna(how='all', subset=['idade', 'nome'])
# %%
#Preenchendo dados faltantes usando fillna

df['idade'].fillna(0) #Aplicando isso para uma série do dataset
df.fillna(0) #Aplica a mudança para todo o dataset
#Aqui podemos selecionar qualquer valor (nesse caso substituimos por 0, mas poderia ser média, 1, etc)
# %%
df.fillna({'nome': 'alguem', 'idade': 0}) #Definindo uma estratégia para cada série do dataframe
# %%
medias = df[['idade', 'salario']].mean()
df.fillna(medias)   #Substituindo os valores numéricos existente pelas respectivas médias de cada um
# %%
