-- SELECT IdProduto,
--         count(*) AS QtdeTransacoes

-- FROM transacao_produto

-- GROUP BY IdProduto

-- Selecionando os 10 cliente que mais pontuaram no mês de julho de 2025. E desses 10, selecionando os que pontuaram mais de 4000 pontos. E ordenando do maior para o menor.
SELECT IdCliente,
        sum(QtdePontos) AS TotalPontos,
        count(*) AS QtdeTransacoes

FROM transacoes 

WHERE DtCriacao >= '2025-07-01'
AND DtCriacao < '2025-08-01'

GROUP BY IdCliente
HAVING TotalPontos >= 4000

ORDER BY TotalPontos DESC

LIMIT 10