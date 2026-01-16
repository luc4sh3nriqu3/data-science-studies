#Objetivo deste código é ler múltiplos arquivos CSV de uma pasta, renomear colunas específicas, definir um índice composto (nome e período) e concatenar todos os DataFrames resultantes em um único DataFrame.
#%%
import pandas as pd
import os

#%%
def read_file(nome_arquivo:str):
    df = (pd.read_csv(f'../../data/ipea/{nome_arquivo}.csv', sep=';')
            .rename(columns={'valor': nome_arquivo})
            .set_index(['nome', 'período'])
            .drop(['cod'], axis=1))
    
    return df

#%%
file_names = os.listdir('../../data/ipea/') #Retorna uma lista com todos os arquivos que estão dentro do caminho especificado
file_names = [i for i in file_names if i.endswith('.csv')] #Filtra apenas os arquivos que terminam com .csv
file_names
#%%
dfs = [] #Lista vazia para armazenar os dataframes
for i in file_names:
    file_name = i.split('.')[0]
    dfs.append(read_file(file_name))

# %%
dfs[-5]
# %%
df_full = pd.concat(dfs, axis=1).reset_index().sort_values(['período', 'nome'])
df_full.to_csv('homicidios_consolidados.csv', index=False, sep=';')
# %%
