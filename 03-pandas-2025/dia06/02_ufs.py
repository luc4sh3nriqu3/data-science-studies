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
#Coluna de alfabetização
def alf_to_percent(p):
    return round( float(p.replace('%', '')
                  .replace(',', '.')) / 100, 3 )

uf['Alfabetização (2016)'] = uf['Alfabetização (2016)'].apply(alf_to_percent)

# %%
uf
# %%

#Mortalidade infantil (por mil habutantes)
# y -- 100
#  x -- 1000 -> 100x = 1000y -> x = 10y
#Ou seja retornaremos um valor 10 vezes maior que o recebido

def mort_to_percent(y):
    return round( float(y.replace('‰', '')
                  .replace(',', '.')) * 10 )


uf['Mortalidade infantil (2016)'] = uf['Mortalidade infantil (2016)'].apply(mort_to_percent)
# %%
uf
# %%
def uf_to_regiao(uf):
    if uf in ['Distrito Federal', 'Goiás', 'Mato Grosso', 'Mato Grosso do Sul']:
        return 'Centro-Oeste'
    
    elif uf in ['Alagoas', 'Bahia', 'Ceará', 'Maranhão', 'Paraíba', 'Pernambuco', 'Piauí', 'Rio Grande do Norte', 'Sergipe']:
        return 'Nordeste'
    
    elif uf in ['Acre', 'Amapá', 'Amazonas', 'Pará', 'Rondônia', 'Roraima', 'Tocantins']:
        return 'Norte'
    
    elif uf in ['Espírito Santo', 'Minas Gerais', 'Rio de Janeiro', 'São Paulo']:
        return 'Sudeste'
    
    elif uf in ['Paraná', 'Rio Grande do Sul', 'Santa Catarina']:
        return 'Sul'

uf['Região'] = uf['Unidade federativa'].apply(uf_to_regiao)
# %%
uf
# %%
