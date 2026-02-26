-- Qual o dia da semana mais ativo de cada usuário?

WITH tb_dia_cliente AS (

    SELECT IdCliente,
           strftime('%w', substr(DtCriacao, 1, 10)) AS DiaSemana,
            count(DISTINCT IdTransacao) AS QtdeTransacao

    FROM transacoes

    GROUP BY IdCliente, DiaSemana

),

tb_rn AS (

    SELECT *,
           CASE
                WHEN DiaSemana = '0' THEN 'Domingo'
                WHEN DiaSemana = '1' THEN 'Segunda-feira'
                WHEN DiaSemana = '2' THEN 'Terça-feira'
                WHEN DiaSemana = '3' THEN 'Quarta-feira'
                WHEN DiaSemana = '4' THEN 'Quinta-feira'
                WHEN DiaSemana = '5' THEN 'Sexta-feira'
                WHEN DiaSemana = '6' THEN 'Sábado'
           END AS DiaSemanaNome,
           row_number() OVER (PARTITION BY IdCliente ORDER BY QtdeTransacao DESC) AS rn

    FROM tb_dia_cliente

)

SELECT IdCliente,
       DiaSemanaNome,
       QtdeTransacao
FROM tb_rn
WHERE rn = 1