-- SELECT *
-- FROM clientes
-- -- Ordena os clientes com base na quantidade de pontos, do maior para o menor
-- ORDER BY QtdePontos DESC
-- LIMIT 10;

SELECT *
FROM clientes
WHERE flTwitch = 1  -- Filtra primeiro antes de ordenar
ORDER BY DtCriacao ASC, QtdePontos DESC