# %%
import pandas as pd
import numpy as np

clientes = pd.read_csv('../data/clientes.csv', sep=';')
clientes.head()
# %%
clientes['pontos_100'] = clientes['qtdePontos'] + 100
# %%
clientes.head()
# %%
clientes['emailTwitch'] = clientes['flEmail'] + clientes['flTwitch']
# %%
clientes.head()
# %%
clientes['flEmail'] * clientes['flTwitch']
# %%
clientes['qtdeSocial'] = clientes['flEmail'] + clientes['flTwitch'] + clientes['flYouTube'] + clientes['flBlueSky'] + clientes['flInstagram']
clientes.head()
# %%
clientes['todas_social'] = clientes['flEmail'] * clientes['flTwitch'] * clientes['flYouTube'] * clientes['flBlueSky'] * clientes['flInstagram']
clientes
# %%
clientes['qtdePontos'].describe()
# %%
clientes['logPontos'] = np.log(clientes['qtdePontos'] + 1)
# %%
clientes['logPontos'].describe()
# %%
