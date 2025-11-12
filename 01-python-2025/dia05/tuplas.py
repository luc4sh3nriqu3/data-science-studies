# %%
#Tupla são listas, porém são imutáveis
dados_lucas =[22, 1, 'Solteiro', 'Eletrônico']
dados_lucas
# %%
dados_lucas.append('2500.50')
dados_lucas
# %%
tupla_lucas = (22, 1, 'Solteiro', 'Eletrônico', ['Lucas', 'Matheus'])
print(type(tupla_lucas))
# %%
tupla_lucas[0] = 10
# %%
tupla_lucas[-1].append('Fodase')
tupla_lucas
# %%
