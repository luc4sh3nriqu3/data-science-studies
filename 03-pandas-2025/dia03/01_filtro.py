# %%
import pandas as pd

df = pd.read_csv('../data/transacoes.csv', sep=';')
df.head()
# %%
pontos = [10, 1, 1, 1, 50, 30, 130, 21, 11, 30, 25, 50, 100]
filtro = []

for i in pontos:
    filtro.append(i>=50)

resultado = []
# %%
for i in range(len(pontos)):
    if filtro[i]:
        resultado.append(pontos[i])
# %%
resultado
# %%
brinquedo = pd.DataFrame(
    {
            'nome': ['Lucas', 'Matheus', 'Pedro'],
            'idade': [22, 17, 3],
            'uf': ['sp', 'pr', 'rj']
    }
)

brinquedo
# %%

filtro = brinquedo['idade'] >= 18 #Montando a série com o resultado das idades maiores que 18

# %%
brinquedo[filtro] #Mostrando somente os elementos que possuem True (ou seja, idades maiores que 18)
# %%
df
# %%
filtro = df['QtdePontos'] >= 50

df[filtro]

# %%
filtro = (df['QtdePontos'] >= 50) & (df['QtdePontos'] < 100)
filtro
# %%
df[filtro]
# %%
filtro = (df['QtdePontos'] == 1) | (df['QtdePontos'] == 100)
df[filtro]
# %%
filtro = (df['QtdePontos'] > 0) & (df['QtdePontos'] <= 50) & (df['DtCriacao'] >= '2025-01-01')
df[filtro]
# %%
