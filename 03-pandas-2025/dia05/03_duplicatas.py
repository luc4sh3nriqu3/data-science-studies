#%%
import pandas as pd

# %%
df = pd.DataFrame({
    'nome': ['Lucas', 'Matheus', 'Pedro', 'Maria', 'Lucas', 'Lucas', 'Deise', 'Lucas'],
    'sobrenome': ['Henrique', 'Henrique', 'Jorge', 'Amorim', 'Henrique', 'Amorim', 'Amorim', 'Henrique'],
    'salario': [6543, 1231, 2431, 2987, 6532, 987, 4322, 2134]
})

df
# %%
df.drop_duplicates() #Mantém a primeira aparição do dado duplicado e exclui as demais

# %%
df.drop_duplicates(keep='last') #Mantém a última duplicata e remove as demais
# %%
df.drop_duplicates(keep='last', subset=['nome', 'sobrenome']) #Considera duplicata nas series selecionadas e não a linha toda

# %%
#Se quisermos remover as duplicatas com base em uma outra coluna, como por exemplo o salário (manter o menor salário)
#vamos primeiro organizar o df com base nos salários para depois remover a duplicata

df = (df.sort_values('salario', ascending=False)
        .drop_duplicates(keep='last', subset=['nome', 'sobrenome']))

df

# %%
