-- Quem iniciou o curso, em média assistiu quantas aulas?

-- Quem participou da 1a aula
WITH tb_prim_dia AS (

    SELECT DISTINCT IdCliente
    FROM  transacoes AS t1
    WHERE substr(t1.DtCriacao, 1, 10) = '2025-08-25'

),

-- Quem participou durante o curso inteiro
tb_dias_curso AS (

    SELECT DISTINCT
            IdCliente,
            substr(DtCriacao, 1, 10) AS PresenteDia
    FROM transacoes
    WHERE DtCriacao >= '2025-08-25'
    AND DtCriacao < '2025-08-30'

    ORDER BY IdCliente, PresenteDia

),

-- Contando quantas vezes quem participou do primeiro dia, voltou
tb_clientes_dias AS (

    SELECT t1.IdCliente,
        count( DISTINCT t2.PresenteDia) AS QtdeDias
    FROM tb_prim_dia AS t1

    LEFT JOIN tb_dias_curso AS t2
    ON t1.IdCliente = t2.IdCliente

    GROUP BY t1.IdCliente

)

SELECT avg(QtdeDias) FROM tb_clientes_dias

