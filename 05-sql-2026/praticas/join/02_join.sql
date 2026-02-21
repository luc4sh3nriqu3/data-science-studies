-- Em 2024, quantas transações de Lovers tivemos?

SELECT count(*)

FROM transacoes as t1

LEFT JOIN transacao_produto AS t2
ON t1.IdTransacao = t2.IdTransacao

INNER JOIN produtos as t3
ON t2.IdProduto = t3.IdProduto
AND t3.DescCategoriaProduto LIKE '%Lover%'

WHERE substr(t1.DtCriacao, 1, 4) = '2024'



