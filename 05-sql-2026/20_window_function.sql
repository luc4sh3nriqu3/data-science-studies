WITH cliente_dia AS (

    SELECT DISTINCT
        IdCliente,
        substr(DtCriacao, 1, 10) AS DtDia

    FROM transacoes

    WHERE substr(DtCriacao, 1, 4) = '2025'

    ORDER BY IdCliente, DtDia

),

tb_lag AS (

    SELECT *,
        lag(DtDia) OVER (PARTITION BY IdCliente ORDER BY DtDia) AS LagDia
    FROM cliente_dia

),

tb_diff_dt AS (

    SELECT *,
        julianday(DtDia) - julianday(LagDia) AS DtDiff
    FROM tb_lag

),

avg_cliente AS (

SELECT IdCliente,
       avg(DtDiff) AS AvgDia

FROM tb_diff_dt
GROUP BY IdCliente

)

SELECT avg(AvgDia) FROM avg_cliente