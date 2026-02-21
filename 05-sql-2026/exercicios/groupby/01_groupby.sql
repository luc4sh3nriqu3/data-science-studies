-- Quantos clientes tem email cadastrado?

-- ======= Alternativa 1 =======
-- SELECT flEmail,
--         count(*)

-- FROM clientes

-- GROUP BY flEmail

-- ORDER BY flEmail DESC

-- LIMIT 1

-- ======= Alternativa 2 =======
SELECT sum(flEmail)

FROM clientes
