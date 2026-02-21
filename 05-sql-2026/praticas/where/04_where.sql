-- Selecione produtos que contêm ‘churn’ no nome
SELECT *

FROM produtos

WHERE DescNomeProduto LIKE 'churn%'; -- o operador LIKE é usado para buscar um padrão específico em uma coluna. O símbolo % é um curinga que representa qualquer sequência de caracteres, permitindo encontrar produtos que contenham 'churn' em qualquer parte do nome.