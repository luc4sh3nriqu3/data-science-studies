#04.03 - Quantas transações ocorreram no dia 2025-02-01?
#%%
import pandas as pd

transacoes = pd.read_csv('../../data/transacoes.csv', sep=';')
transacoes.head()
# %%
#Primeiro, vamos converter a data de criação para o formato datetime
replace = {
    '0000-00-00 00:00:00.000': '2025-11-11 22:50:00.000'
}

transacoes['DtCriacao'] = pd.to_datetime(transacoes['DtCriacao'].replace(replace))
transacoes['DtCriacao']

#Após convertido vamos salvar a data que queremos filtrar
filtro = transacoes['DtCriacao'].dt.date == pd.to_datetime('2025-02-01').date()
# %%
print(f'Quantidade de transações no dia 2025-02-01: {transacoes[filtro].shape[0]}')
# %%
