SELECT 
    count(*), -- total de transações no mês de julho de 2025
    count(DISTINCT IdTransacao), -- total de transações distintas no mês de julho de 2025
    count(DISTINCT IdCliente) -- total de clientes distintos que realizaram transações no mês de julho de 2025

FROM transacoes

WHERE DtCriacao >= '2025-07-01'
AND DtCriacao < '2025-08-01'