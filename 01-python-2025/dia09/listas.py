# %%

lista = [i for i in range(1, 101)]
lista
# %%

def eh_par(x):
    return x % 2 == 0

lista2 = [eh_par(i) for i in range(1, 101)]
lista2
# %%

lista3 = [i for i in range(1, 101) if eh_par(i)]
lista3
# %%
