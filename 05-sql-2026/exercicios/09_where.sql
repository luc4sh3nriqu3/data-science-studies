SELECT IdTransacao,
       QtdePontos,
       CASE
            WHEN QtdePontos < 10 THEN 'baixo'
            WHEN QtdePontos < 500  THEN 'médio'
            ELSE 'alto'
        END AS NivelPontos

FROM transacoes

ORDER BY QtdePontos DESC