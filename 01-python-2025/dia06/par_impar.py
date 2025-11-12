# %%
def paridade(numero: int):
    if(numero % 2 == 0):
        return f'o número {numero} é par'
    
    return f'o número {numero} é ímpar'
# %%

numero = int(input('Digite um número: '))

analise = paridade(numero)

print(analise)
# %%
