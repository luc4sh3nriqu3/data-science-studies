-- Quais clientes mais perderam pontos por Lover?
SELECT t1.IdCliente,
        sum(t1.QtdePontos) as TotalPontos

FROM transacoes as t1

LEFT JOIN transacao_produto as t2
ON t1.IdTransacao = t2.IdTransacao

INNER JOIN produtos as t3
ON t2.IdProduto = t3.IdProduto
AND t3.DescCategoriaProduto = "lovers"

GROUP BY t1.IdCliente

ORDER BY 2

LIMIT 5
