#%%
a = 1
b = 5
print(a, b)

#Queremos inverter os valores de a e b
# %%

c = a
a = b
b = c

print(a, b)

# %%
#Usando unpack
a, b = b, a
print(a, b)
# %%
a, b = 1, ['cu', 'pinto']
print(a, b)
# %%
a, b, c, d = 1, 2, 3, 4
print(a, b, c, d)
# %%
a, b, *resto = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
print(a, b, resto)
# %%
*resto, a, b = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
print(resto, a, b)
# %%
a, *resto, b = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
print(a, resto, b)
# %%

def soma(a, *args):
    return a + sum(args)

soma(1, 2, 3, 4)
# %%

def soma_quatro (a, b, c, d):
    return a+b+c+d

lista = [1, 2, 3, 4]
# %%
soma_quatro(lista) #Não funciona
# %%
soma_quatro(*lista) #Funciona
soma(*lista)
# %%
