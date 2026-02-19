SELECT avg(QtdePontos) AS MediaPontos,
        min(QtdePontos) AS MinimoPontos,
        max(QtdePontos) AS MaximoPontos,
        sum(flTwitch) AS QtdeTwitch,
        sum(flEmail) AS QtdeEmail

FROM clientes