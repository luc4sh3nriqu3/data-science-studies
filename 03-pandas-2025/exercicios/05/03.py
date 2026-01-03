#05.03 - Crie uma coluna que sinalize se a pessoa tem vínculo com alguma (qualquer uma) plataforma de rede social.
#%%
import pandas as pd

clientes = pd.read_csv('../../data/clientes.csv', sep=';')
clientes.head()
# %%
def possui_vinculo(linha):
    return(
        linha['flEmail'] == 1 or
        linha['flTwitch'] == 1 or
        linha['flYouTube'] == 1 or
        linha['flBlueSky'] == 1 or
        linha['flInstagram'] == 1
    )

clientes['PossuiVinculo'] = clientes.apply(possui_vinculo, axis=1) # axis=1 para aplicar por linha e acessar o conteudo de varias colunas ao mesmo tempo
clientes['PossuiVinculo'].value_counts()
# %%
clientes.head()
# %%
