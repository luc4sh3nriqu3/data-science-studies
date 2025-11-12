# %%

#Pares de chave/valor
dados_lucas = {
    'nome': 'Lucas', 
    'Filhos':True,
    'formacao': ['Automacao', 'Computacao', 'Sexologia'],
    'cargos': [
        {'nome': 'Auxiliar Adm', 'empresa': 'Rand'},
        {'nome': 'Motoboy', 'empresa': 'Pizzaria'},
        {'nome': 'Técnico Robótica', 'empresa': 'MPS'},
        {'nome': 'Estag. Data Science', 'empresa': 'Itau'},
    ]
    }

print(dados_lucas)
# %%
print(dados_lucas['nome'])
# %%
print(dados_lucas['formacao'][-1])
# %%
print(dados_lucas['cargos'][-1]['empresa'])
# %%
dados_lucas['estado civil'] = 'solteiro'

print(dados_lucas)

# %%
print('Chaves: ', dados_lucas.keys()) #Lista todas as chaves de um dicionário
print('Valores: ', dados_lucas.values()) #Lista os valores de um dicionário
print('Itens: ', dados_lucas.items()) #Retorna tuplas de chave e valor
# %%

#Percorrendo um dicionário
for i in dados_lucas:
    print(i, '->', dados_lucas[i])
# %%

for chave, valor in dados_lucas.items():
    print(chave, '->', valor)
# %%
