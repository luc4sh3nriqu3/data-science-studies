#06.04 - Quem teve mais transações de Streak?
#%%
import pandas as pd

# %%
#INFORMAÇÕES GERAIS SOBRE AS TRANSAÇÕES
transacoes = pd.read_csv('../../data/transacoes.csv', sep=';')
transacoes.head()
# %%
#CONTÉM INFORMAÇÕES SOBRE AS TRANSAÇÕES REALIZADAS EM CADA PRODUTO (LIGA O CLIENTE AO PRODUTO)
transacao_produto = pd.read_csv('../../data/transacao_produto.csv', sep=';')
transacao_produto.head()
# %%
#CONTÉM INFORMAÇÕES SOBRE OS PRODUTOS
produtos = pd.read_csv('../../data/produtos.csv', sep=';')
produtos.head()
# %%
#PRIMEIRO VAMOS FAZER O MERGE ENTRE AS TABELAS TRANSACOES E TRANSACAO_PRODUTO
#PARA VINCULAR O ID DO CLIENTE AO ID DO PRODUTO
cliente_transacao_produto = transacoes.merge(
    transacao_produto, 
    on='IdTransacao',
    how='left',
)

#Pegando apenas as colunas necessárias depois do merge
cliente_transacao_produto = cliente_transacao_produto[['IdTransacao', 'IdCliente', 'IdProduto']]
cliente_transacao_produto.head()
# %%
cliente_transacao_produto['IdProduto'].value_counts()
# %%

cliente_transacao_produto.merge(
    produtos,
    on='IdProduto'
)

#Aqui, ao tentar fazer o merge, percebemos que a coluna IdProduto possui valores NaN.
#Após analisar os dados, percebemos que esses NaN correspondem a transações que não possuem ID da maneira correta,
#Ao dar um "cliente_transacao_produto['IdProduto'].value_counts()" vemos que existem IDs que estão da seguinte maneira:
#'github-2025', 'python-2025', 'sql-2025', 'estatistica-2025', 'pandas-2025' e 'machine-learning-2025'.
#Esses IDs não existem na tabela produtos, por isso o merge não funciona corretamente.
#Iremos substituir esses valores para conseguir realizar o merge da maneira correta.
# %%
def corrigir_id_produto(id_produto):
    if '-2025' in str(id_produto):
        return 5 #ID com maior número de transações
    elif '-2024' in str(id_produto):
        return 5 #ID com maior número de transações
    return pd.to_numeric(id_produto, errors='coerce')
#%%
 

cliente_transacao_produto['IdProduto'] = cliente_transacao_produto['IdProduto'].apply(corrigir_id_produto)
cliente_transacao_produto['IdProduto'].value_counts()


# %%
#Agora que removemos os valores incorretos, podemos fazer o merge corretamente
df_full = cliente_transacao_produto.merge(
    produtos,
    on=['IdProduto'],
    how='left'
)
# %%
df_full = df_full[['IdTransacao', 'IdCliente', 'IdProduto', 'DescNomeProduto']]
df_full['DescNomeProduto'].value_counts()
# %%
#Agora vamos filtrar apenas as transações do produto Streak
df_full = df_full[df_full['DescNomeProduto'] == 'Presença Streak']
df_full
# %%
#Agora vamos utilizar o groupby para separar por cliente e contar o número de transações (organizando elas da maior para a menor, pegando o cliente com mais transações no topo)
(df_full.groupby(by=['IdCliente'])['IdTransacao']
    .count()
    .sort_values(ascending=False)
    .head(1)
)
# %%
