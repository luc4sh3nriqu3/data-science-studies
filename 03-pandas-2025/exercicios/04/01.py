#04.01 - Quantos clientes tem vínculo com a Twitch?
#%%
import pandas as pd

clientes = pd.read_csv('../../data/clientes.csv', sep=';')

clientes.head()
# %%
tem_twitch = clientes['flTwitch'] == 1
print("Quantidade de clientes com vínculo com a Twitch:", clientes[tem_twitch].shape[0])
# %%
