-- Lista de clientes com 0 (zero) pontos

SELECT idCliente,
        QtdePontos

FROM clientes

WHERE QtdePontos = 0;