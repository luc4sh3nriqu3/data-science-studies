SELECT substr(t1.DtCriacao, 1, 7) as MesAnoTransacao,
        count(t1.IdTransacao) AS QuantidadePresenca

FROM transacoes as t1

LEFT JOIN transacao_produto as t2
ON t1.IdTransacao = t2.IdTransacao

INNER JOIN produtos as t3
ON t2.IdProduto = t3.IdProduto
AND t3.DescNomeProduto = 'Lista de presença'

GROUP BY substr(t1.DtCriacao, 1, 7)

ORDER BY 2 DESC