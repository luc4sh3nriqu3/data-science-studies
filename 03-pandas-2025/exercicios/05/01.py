#05.01 - Crie uma coluna nova “twitch_points” que e resultado da multiplicação do saldo de pontos e a marcação da twitch
#%%
import pandas as pd

transacoes = pd.read_csv('../../data/transacoes.csv', sep=';')
transacoes.head(n=20)
# %%

#USANDO UMA FUNÇÃO COM APPLY (transformaremos usuarios de Twitch em 1 (para poder multiplicar depois) e os outros em 0)
def is_twitch_user(descSistemaOrigem):
    if descSistemaOrigem.lower() == 'twitch':
        return 1
    return 0

transacoes['isTwitchUser'] = transacoes['DescSistemaOrigem'].apply(is_twitch_user)
transacoes['isTwitchUser'].value_counts() #Verificando quantos usuários são twitch e quantos não são

# %%
transacoes['twitch_points'] = transacoes['QtdePontos'] * transacoes['isTwitchUser']
transacoes.head(n=20)
# %%
