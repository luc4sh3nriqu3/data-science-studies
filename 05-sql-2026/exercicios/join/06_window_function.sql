-- Quantidade de usuários cadastrados (absoluto e acumulado) ao longo do tempo

WITH tb_clientes_dia AS (

    SELECT substr(DtCriacao, 1, 10) AS DtDia,
        count(DISTINCT IdCliente) AS QtdeNovosClientes

    FROM clientes

    GROUP BY DtDia
    ORDER BY DtDia

),

tb_lag AS (

    SELECT *,
        lag(QtdeNovosClientes) OVER (ORDER BY DtDia) AS LagNovosClientes

    FROM tb_clientes_dia

)

SELECT DtDia,
       QtdeNovosClientes,
       sum(QtdeNovosClientes) OVER (ORDER BY DtDia) AS ClientesAcum,
       1. * QtdeNovosClientes / LagNovosClientes AS CientesAbs

FROM tb_lag