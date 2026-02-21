-- Qual cliente fez mais transações no ano de 2024

SELECT IdCliente,
        count(IdTransacao)

FROM transacoes

WHERE DtCriacao > '2023-31-12'
AND DtCriacao <= '2024-31-12'

GROUP BY IdCliente

ORDER BY count(IdTransacao) DESC

LIMIT 1