WITH tb_cliente_dia AS (

    SELECT IdCliente,
        substr(DtCriacao, 1, 10) AS DtDia,
        count(DISTINCT IdTransacao) AS QtdeTransacao

    FROM transacoes
    WHERE DtCriacao >= '2025-08-25'
    AND DtCriacao < '2025-08-30'

    GROUP BY IdCliente, DtDia

),

tb_lag AS (

    SELECT *,
        sum(QtdeTransacao) OVER (PARTITION BY IdCliente ORDER BY DtDia) AS Acum,
        lag(QtdeTransacao) OVER (PARTITION BY IdCliente ORDER BY DtDia) AS LagTransacao
    FROM tb_cliente_dia

)

SELECT *,
       1. * QtdeTransacao / LagTransacao
FROM tb_lag