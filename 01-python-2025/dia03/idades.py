# %%
idades = []

while True:
    idade = input('Entre com uma idade: ')

    if (idade == ''):
        break
    
    idades.append(int(idade))

print('Idades adicionadas: ', idades)
# %%
