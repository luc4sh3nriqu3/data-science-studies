# %%
import pandas as pd

clientes = pd.read_csv('../data/clientes.csv', sep=';')
clientes
# %%
filtro = clientes['qtdePontos'] == 0
clientes_0 = clientes[filtro] #Atribuindo o resultado do filtro a uma variável
clientes_0
# %%
clientes_0['flag_1'] = 1
# %%

#IMPORTANTE: clientes_0 não é um novo dataset copiado de clientes com apenas as linhas escolhidas, ele é uma view do dataset inicial. Então as linhas dele apontam para as mesmas linhas do dataset inicial, porém elas apontam apenas para as linhas filtradas.
#Se quisermos realmente criar uma cópia do dataset filtrado usamos o seguinte comando:
clientes_0 = clientes[filtro].copy()
# %%
clientes_0['flag_1'] = 1

# %%
