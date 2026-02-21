SELECT t1.*,
        t2.DescNomeProduto

FROM transacao_produto AS t1

INNER JOIN produtos AS t2
ON t1.IdProduto = t2.IdProduto

