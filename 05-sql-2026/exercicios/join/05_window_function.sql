-- Quantidade de transações Acumuladas ao longo do tempo

WITH transacoes_dia AS (

    SELECT substr(DtCriacao, 1, 10) AS DtDia,
        count(DISTINCT IdTransacao) AS QtdeTransacao

    FROM transacoes

    GROUP BY DtDia

    ORDER BY DtDia

),

tb_acum AS (

    SELECT *,
        sum(QtdeTransacao) OVER (ORDER BY DtDia) QtdeTransacaoAcum

    FROM transacoes_dia

)

-- Quando bateu 100000 transações?
-- SELECT *
-- FROM tb_acum
-- WHERE QtdeTransacaoAcum > 100000
-- ORDER BY QtdeTransacaoAcum
-- LIMIT 1

SELECT * FROM tb_acum