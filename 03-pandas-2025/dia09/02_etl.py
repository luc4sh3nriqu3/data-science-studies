#%%
import pandas as pd
import sqlalchemy
from sklearn import cluster
#%%
with open("etl.sql") as open_file:
    query = open_file.read()

print(query)
# %%

engine = sqlalchemy.create_engine('sqlite:///../data/olist.db')

df = pd.read_sql_query(sql=query, con=engine)
# %%
df
# %%
#PROCESSAMENTO DE DADOS COM KMEANS
kmeans = cluster.KMeans(n_clusters=4,)
kmeans.fit(df[['totalRevenue', 'qtSalles']])

kmeans.labels_
# %%
df['cluster'] = kmeans.labels_
# %%
df
# %%
#DEVOLVENDO OS DADOS PARA O BANCO DE DADOS (ATUALIZANDO COM A NOVA COLUNA) DEPOIS DO PROCESSAMENTO
df.to_sql("sellers_cluster", con=engine, index=False, if_exists='replace')