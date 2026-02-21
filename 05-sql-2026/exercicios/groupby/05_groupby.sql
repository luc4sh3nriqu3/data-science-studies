-- Qual o valor médio de pontos positivos por dia?

SELECT sum(QtdePontos) AS TotalPontos,
        count( DISTINCT substr(DtCriacao, 1, 10)) AS TotalDias,
        sum(QtdePontos) / count( DISTINCT substr(DtCriacao, 1, 10)) AS MediaPorDia

FROM transacoes

WHERE QtdePontos > 0



