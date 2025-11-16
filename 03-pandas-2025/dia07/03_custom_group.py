#%%
import pandas as pd
import numpy as np
from sqlalchemy.sql.operators import as_

transacoes = pd.read_csv('../data/transacoes.csv', sep=';')
transacoes.head()
# %%

def diff_amp(x: pd.Series):
    amplitude = x.max() - x.min()
    media = x.mean()
    return np.sqrt((amplitude - media) ** 2) #métrica personalizada

idades = [15, 22, 35, 45, 52, 63, 70, 80, 12, 33, 47, 58, 69, 74, 81]
idades = pd.Series(idades)

diff_amp(idades)
# %%
def life_time (x: pd.Series):
    dt = pd.to_datetime(x)
    return (dt.max() - dt.min()).days
# %%


summary = (transacoes.groupby(by='IdCliente', as_index=False) 
            .agg({
                'IdTransacao': ['count'],
                'QtdePontos': ['mean', 'sum', diff_amp],
                'DtCriacao': [life_time]
            })

)
# %%
summary.columns = ['IdCliente', 'QtdeTransacoes', 'MediaPontos', 'TotalPontos', 'DiffAmpPontos', 'LifeTime']
summary
# %%
