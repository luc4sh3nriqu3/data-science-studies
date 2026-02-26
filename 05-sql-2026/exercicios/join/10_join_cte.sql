-- Como foi a curva de CHURN do curso de SQL?

-- SELECT substr(DtCriacao, 1, 10) AS DtDia,
--        count(DISTINCT IdCliente) AS QtdeCliente

-- FROM transacoes
-- WHERE DtCriacao >= '2025-08-25'
-- AND DtCriacao < '2025-08-30'

-- GROUP BY DtDia

WITH tb_clientes_d1 AS (

    SELECT DISTINCT IdCliente
    FROM transacoes
    WHERE substr(DtCriacao, 1, 10) = '2025-08-25'
),

tb_join AS (

    SELECT substr(t2.DtCriacao, 1, 10) AS DtDia,
        count(DISTINCT t1.IdCliente) AS QtdeClientes,
        1. * count(DISTINCT t1.IdCliente) / (SELECT count(*) FROM tb_clientes_d1) AS PctRetencao,
        1 - 1. * count(DISTINCT t1.IdCliente) / (SELECT count(*) FROM tb_clientes_d1) AS PctChurn
            

    FROM tb_clientes_d1 AS t1
    LEFT JOIN transacoes as t2
    ON t1.IdCliente = t2. IdCliente

    WHERE t2.DtCriacao >= '2025-08-25'
    AND DtCriacao < '2025-08-30'

    GROUP BY 1
)

SELECT * FROM tb_join