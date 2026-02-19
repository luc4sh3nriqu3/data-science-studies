SELECT 
        sum(QtdePontos),
        
        sum(CASE
            WHEN QtdePontos > 0 THEN QtdePontos
            END) AS PontosPositivos,

        sum(CASE
            WHEN QtdePontos < 0 THEN QtdePontos
            END) AS PontosNegativos,
        
        count(CASE
            WHEN QtdePontos > 0 THEN QtdePontos
            END) AS QtdePontosPositivos,

        count(CASE
            WHEN QtdePontos < 0 THEN QtdePontos
            END) AS QtdePontosNegativos


FROM transacoes
WHERE DtCriacao >= '2025-07-01'
AND DtCriacao < '2025-08-01'