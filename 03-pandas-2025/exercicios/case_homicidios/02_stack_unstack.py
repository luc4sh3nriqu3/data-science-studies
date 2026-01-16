#%%
import pandas as pd

df = pd.read_csv('homicidios_consolidados.csv', sep=';')
#%%
df
# %%
#STACK - Transforma colunas em linhas para que o eu não precise adicionar uma nova métrica
df = df.set_index(['nome', 'período'])
df_stack = df.stack() #retorna uma Series
# %%
df_stack = df_stack.reset_index() #Retorna o valor da série para Dataframe
# %%
df_stack.columns = ["nome", "período", "métrica", "valor"]
df_stack
# %%
#UNSTACK - Transforma linhas em colunas
df_unstack = (df_stack.set_index(['nome', 'período', 'métrica'])
                      .unstack()
                      .reset_index())
df_unstack.columns
# %%
metricas = df_unstack.columns.droplevel(0)[2:].tolist()  # Remove o nível 0 do MultiIndex das colunas após o unstack
df_unstack.columns = ['nome', 'período'] + metricas
# %%
df_unstack
# %%
