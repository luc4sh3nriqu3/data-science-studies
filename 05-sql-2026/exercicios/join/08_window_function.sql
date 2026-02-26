-- Saldo de pontos acumulado de cada usuário

WITH clientes_pontos_dia AS (

    SELECT IdCliente,
        substr(DtCriacao, 1, 10) AS DtDia,
        sum(QtdePontos) AS QtdePontosDia

    FROM transacoes

    GROUP BY IdCliente, DtDia

)

SELECT IdCliente,
       DtDia,
       QtdePontosDia,
       sum(QtdePontosDia) OVER (PARTITION BY IdCliente ORDER BY DtDia) AS QtdePontosAcum
FROM clientes_pontos_dia