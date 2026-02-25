-- Do início ao fim do nosso curso (2025/08/25 a 2025/08/29),
--quantos clientes assinaram a lista de presença?

SELECT t1.IdCliente,
        count(*)

FROM transacoes AS t1

LEFT JOIN transacao_produto AS t2
ON t1.IdTransacao = t2.IdTransacao

INNER JOIN produtos AS t3
ON t2.IdProduto = t3.IdProduto
AND t3.DescNomeProduto = 'Lista de presença'

WHERE substr(t1.DtCriacao, 1, 10) > '2025-08-24'
AND substr(t1.DtCriacao, 1, 10) <= '2025-08-29'

GROUP BY IdCliente

ORDER BY 2 DESC

