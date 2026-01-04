#Resolvendo o exercício 4 de uma forma mais avançada e mais performática
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

def corrigir_id_produto(id_produto):
    if '-2025' in str(id_produto):
        return 5 #ID com maior número de transações
    elif '-2024' in str(id_produto):
        return 5 #ID com maior número de transações
    return pd.to_numeric(id_produto, errors='coerce')

transacao_produto['IdProduto'] = transacao_produto['IdProduto'].apply(corrigir_id_produto)
# %%
#CONTÉM INFORMAÇÕES SOBRE OS PRODUTOS
produtos = pd.read_csv('../../data/produtos.csv', sep=';')
produtos.head()
# %%
#PRIMEIRO, VAMOS APLICAR UM FILTRO NOS PRODUTOS
produtos = produtos[produtos['DescNomeProduto'] == 'Presença Streak']
produtos
# %%
(   #Primeiro merge
    transacoes.merge(
    transacao_produto, 
    on='IdTransacao',
    how='left',
    )
    #Segundo merge
    .merge(produtos, on='IdProduto', how='right')
    #Aplicando o filtro para pegar apenas as transações do produto Streak (por isso colocamos how='right' no segundo merge)
    #Agora, faremos o groupby para contar as transações por cliente
    .groupby(by='IdCliente')['IdTransacao']
    .count()
    .sort_values(ascending=False)
    .head(1)

)
# %%