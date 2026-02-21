-- Quantos produtos são de rpg?

SELECT DescCategoriaProduto,
        count(DescCategoriaProduto)

FROM produtos

WHERE DescCategoriaProduto = 'rpg'

GROUP BY DescCategoriaProduto