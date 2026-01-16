#%%
import pandas as pd
import sqlalchemy

# %%
engine = sqlalchemy.create_engine('sqlite:///../data/olist.db') #Define a conexão do pandas com o banco de dados SQLite

#%%
clientes = pd.read_sql_table(table_name='tb_customers', #Lê a tabela 'tb_customers' do banco de dados SQLite
                             con=engine)                #Através da conexão definida anteriormente
# %%
clientes.shape
# %%
#IMPORTATE: Em ambiente de trabalho, não é recomendado puxar todo o bd pois existem lugares que possuem milhoes ou até bilhões de dados
#E ao puxar tudo de uma vez, podemos travar a memória do python ou sql
#Para evitar isso, executaremos uma query

query = 'SELECT * FROM tb_customers LIMIT 100'

df_100 = pd.read_sql_query(sql=query, con=engine)
# %%
df_100.shape
# %%
