# %%
import pandas as pd

transacoes = pd.read_csv('../data/transacoes.csv', sep=';')
transacoes
# %%
transacoes.groupby(by='IdCliente').count()
# %%
transacoes.groupby(by='IdCliente')['IdTransacao'].count() #Retorna uma série com a quatidade de transações cada cliente fez
transacoes.groupby(by='IdCliente')[['IdTransacao']].count() #Retorna um dataframe com a quatidade de transações cada cliente fez
# %%
summary = (transacoes.groupby(by='IdCliente', as_index=False) #Multiplas agregações agrupando por cliente
            .agg({'IdTransacao': ['count'],
                  'QtdePontos': ['sum', 'mean']})
)

summary
# %%
summary.columns
# %%
summary['QtdePontos']['sum'] #Acessando a coluna de soma de pontos
# %%
#Renomeando as colunas para retirar o multiindex
summary.columns = ['IdCliente', 'QtdeTransacoes', 'TotalPontos', 'MediaPontos']
summary
# %%
