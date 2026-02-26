-- Dentre os clientes de janeiro/2025, quantos assistiram o curso de SQL?

-- Pegando todos os clientes que iniciaram em Janeiro/2025
WITH tb_cli_jan AS (

    SELECT DISTINCT IdCliente
    FROM transacoes
    WHERE DtCriacao >= '2025-01-01'
    AND DtCriacao < '2025-02-01'
),

-- Quantas pessoas participaram do curso
tb_particip_curso AS (

    SELECT DISTINCT
           IdCliente,
           count( DISTINCT substr(DtCriacao, 1, 10)) as PresencaDia
           
    FROM transacoes
    WHERE DtCriacao >= '2025-08-25'
    AND DtCriacao < '2025-08-30'

    GROUP BY 1
),

-- Clientes que são de janeiro e participaram do curso
tb_cli_jan_curso AS (

    SELECT t1.IdCliente AS ClienteJan,
           t2.IdCliente AS ClienteCurso
    FROM tb_cli_jan AS t1
    LEFT JOIN tb_particip_curso AS t2
    ON t1.IdCliente = t2.IdCliente
)

SELECT count(ClienteJan) AS QtdeClientesJaneiro,
       count(ClienteCurso) AS QtdeClientesCurso
FROM tb_cli_jan_curso