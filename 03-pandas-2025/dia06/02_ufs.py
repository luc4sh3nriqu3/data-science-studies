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

uf = dfs[1]
uf
# %%
uf.dtypes
# %%

def str_to_float(x:str):
    x = float(
        x.replace(' ', '')
        .replace(',', '.')
        .replace('\xa0', '')
    ) #Alterando a estrutura escrita do número para podermos aplicar a função float
    return x

# %%
uf['Área (km²)'] = uf['Área (km²)'].apply(str_to_float) #Aplicando a tranformação
uf['População (Censo 2022)'] = uf['População (Censo 2022)'].apply(str_to_float)
uf['PIB (2015)'] = uf['PIB (2015)'].apply(str_to_float)
uf['PIB per capita (R$) (2015)'] = uf['PIB per capita (R$) (2015)'].apply(str_to_float)


# %%
uf.dtypes
# %%
#Fazendo apply para expectativa de vida

def exp_to_anos(exp):
    return float(exp.replace(',', '.').replace(' anos', ''))
# %%
uf['Expectativa de vida (2016)'] = uf['Expectativa de vida (2016)'].apply(exp_to_anos)
# %%
uf
# %%
