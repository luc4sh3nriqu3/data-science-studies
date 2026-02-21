-- Qual o produto com mais pontos transacionados?

SELECT IdProduto,
        sum(vlProduto * QtdeProduto) AS TotalPontoProduto

FROM transacao_produto

GROUP BY IdProduto

ORDER BY 2 DESC

LIMIT 1