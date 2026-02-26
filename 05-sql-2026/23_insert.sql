-- Limpando a tabela (para atualizarmos na query abaixo com dados atualizados)
DELETE FROM relatorio_diario;

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

--Inserindo os dados novos na tabela criada
INSERT INTO relatorio_diario

SELECT * FROM tb_acum;

--Mostrando a tabela nova atualizada
SELECT * FROM relatorio_diario;