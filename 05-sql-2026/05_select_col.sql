SELECT idCliente,
        
        QtdePontos,
        -- Criando uma coluna nova com o resultado da soma de Pontos + 10
        QtdePontos + 10 AS QtdePontosPlus10,
        QtdePontos * 2 AS QtdePontosTimes2,
        
        DtCriacao,
        -- Pega uma parte da string, nesse caso a data sem a hora, pegando os 10 primeiros caracteres 
        -- da string e aplica a função datetime para converter a string em um formato de data
        datetime(substr(DtCriacao, 1, 19)) AS DtCriacaoNova,
        strftime('%w', datetime(substr(DtCriacao, 1, 19))) AS DiaSemana

FROM clientes;