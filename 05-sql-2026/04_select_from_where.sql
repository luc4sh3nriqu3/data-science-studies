SELECT *

FROM produtos

WHERE DescCategoriaProduto = 'rpg' -- aspas simples acessa o valor de um campo (linhas da coluna), aspas duplas acessa o nome do campo

LIMIT 10;

SELECT *

FROM clientes

WHERE clienteIdade >= 18

LIMIT 10;