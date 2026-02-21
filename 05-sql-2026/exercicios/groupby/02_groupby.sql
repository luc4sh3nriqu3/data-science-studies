-- Qual cliente juntou mais pontos em 2025-05?

-- ========= ALTERNATIVA 1 =========
-- SELECT IdCliente,
--         sum(CASE
--             WHEN QtdePontos > 0 THEN QtdePontos
--             END) AS TotalPontosPositivos

-- FROM transacoes

-- WHERE DtCriacao >= '2025-05-01'
-- AND DtCriacao < '2025-06-01'

-- GROUP BY IdCliente

-- ORDER BY TotalPontosPositivos DESC

-- LIMIT 1


-- ========= ALTERNATIVA 2 =========
SELECT IdCliente,
        sum(QtdePontos)

FROM transacoes

WHERE DtCriacao >= '2025-05-01'
AND DtCriacao < '2025-06-01'
AND QtdePontos > 0

GROUP BY IdCliente

ORDER BY sum(QtdePontos) DESC

LIMIT 1