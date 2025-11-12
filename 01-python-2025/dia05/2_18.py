# %%
dicionario = {}

while True:

    frase = input('Digite uma frase: ')

    if(frase != ""):
        if frase in dicionario:
            dicionario[frase] += 1
        else:
            dicionario[frase] = 0
    else:
        break

print(dicionario)
# %%
