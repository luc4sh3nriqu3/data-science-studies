-- Qual dia da semana que tem mais pedidos em 2025

SELECT strftime('%w', substr(DtCriacao, 1, 19)) AS DiaSemana,
        count(DISTINCT IdTransacao) AS QtdeTransacoes

FROM transacoes

WHERE DtCriacao < '2026-01-01'
AND DtCriacao >= '2025-01-01'

GROUP BY 1

ORDER BY 2 DESC

LIMIT 1