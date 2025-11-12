# %%
import requests #Para realizar requisições na web
import json     #Para tratar json de lista/dicionários para arquivos JSON
from tqdm import tqdm #Para mostrar a barra de progresso na execução do for

# %%
ceps = ['12247820',
        '01519000',
        '13329120',
        '14400760',
        '19060100',
        '13600110',
        '21870370',
        '21645522'
]

url = 'https://viacep.com.br/ws/{cep}/json/'
dados = []

for i in tqdm(ceps):

    resposta = requests.get(url.format(cep=i)) #consumir um dado da api

    if resposta.status_code == 200: #response[200] significa que a requisição foi feita e o site retornou a requisição da maneira correta

        dados.append(resposta.json())

# %%
#Salvando os dados
with open('ceps.json', 'w', encoding='utf-8') as open_file:
    json.dump(dados, open_file, ensure_ascii=False, indent=4)
# %%
