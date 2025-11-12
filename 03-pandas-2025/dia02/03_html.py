# %%
# %%
import pandas as pd
import requests

url = 'https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil'

# Define um cabeçalho simulando um navegador
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}

# Faz a requisição manualmente com requests
response = requests.get(url, headers=headers)

# Lê as tabelas a partir do conteúdo da página
dfs = pd.read_html(response.text) #Retorna uma lista de dataframes que ele encontrou na página

dfs

# %%
len(dfs)
# %%
type(dfs)
# %%
df_uf = dfs[1]
df_uf.to_csv('ufs.csv', index=False, sep=';')
# %%
