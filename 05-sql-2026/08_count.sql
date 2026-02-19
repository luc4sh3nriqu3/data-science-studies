-- SELECT count(*),
--         count(1)
-- FROM clientes

-- -- Trás todos os clientes distintos, ou seja, sem repetição
-- SELECT DISTINCT flEmail, flTwitch
-- --Aqui, ele trará os valores distintos considerando as duas colunas, ou seja, avaliará as combinações distintas entre as duas colunas. Se houver um email repetido, mas com um twitch diferente, ambos serão considerados distintos.

-- FROM clientes

SELECT COUNT(DISTINCT flEmail)

FROM clientes