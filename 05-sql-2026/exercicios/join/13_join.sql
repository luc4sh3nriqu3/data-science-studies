-- Qual o dia com maior engajamento de cada aluno que iniciou o curso no 
-- dia 01?

WITH alunos_dia01 AS (

    SELECT DISTINCT IdCliente
    FROM transacoes
    WHERE substr(DtCriacao, 1, 10) = '2025-08-25'

),

tb_dia_cliente AS (

    SELECT t1.IdCliente,
        substr(t2.DtCriacao, 1, 10) AS DtDia,
        count(*) AS Engajamento

    FROM alunos_dia01 AS t1

    LEFT JOIN transacoes AS t2
    ON t1.IdCliente = t2.IdCliente
    AND t2.DtCriacao >= '2025-08-25'
    AND t2.DtCriacao < '2025-08-30'

    GROUP BY t1.IdCliente, DtDia

    ORDER BY t1.IdCliente, Engajamento

),

-- Método 1: Subconsulta

-- max_inter AS (

--     SELECT IdCliente,
--         max(Engajamento) AS MaxInter

--     FROM tb_dia_cliente
--     GROUP BY IdCliente

-- )

-- SELECT t1.IdCliente,
--        max(t2.DtDia) AS MaxDia,
--        max(t1.MaxInter) AS MaxInter

-- FROM max_inter AS t1

-- LEFT JOIN tb_dia_cliente AS t2
-- ON t1.IdCliente = t2.IdCliente
-- AND t1.MaxInter = t2.Engajamento

-- GROUP BY t1.IdCliente
-- ORDER BY t1.IdCliente;


-- Método 2: Row_Number (Window function) - mais performático
tb_rn AS (

    SELECT *,
        row_number() OVER (PARTITION BY IdCliente ORDER BY Engajamento DESC) AS rn

    FROM tb_dia_cliente

)

SELECT *
FROM tb_rn
WHERE rn = 1