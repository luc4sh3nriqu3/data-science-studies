#%%
import pandas as pd

df = pd.read_csv('homicidios_consolidados.csv', sep=';')
# %%
df.head()
# %%
df_stack = (df.set_index(['nome', 'período'])
              .stack()
              .reset_index()
)

# %%
df_stack.columns = ['nome', 'período', 'métrica', 'valor']
# %%
df_stack.head()
# %%
#Aqui devemos pensar como se estivessemos no excel, definimos o que vai nos valores das células (values), #o que vai nas linhas (index) e o que vai nas colunas (columns)
(df_stack.pivot_table(values='valor', 
                     index=['nome', 'período'],
                     columns='métrica')
                     .reset_index())
# %%
(df_stack.pivot_table(values='valor',
                      index=['nome'],
                      columns='métrica',
                      aggfunc='mean', #Estamos retirando a dimensão de período, então precisamos agregar os valores para que ele seja representado de alguma forma (média nesse caso, ou seja, vai pegar a média de todos os períodos pra cada métrica pra aquele estado)
                      ).stack())
# %%
