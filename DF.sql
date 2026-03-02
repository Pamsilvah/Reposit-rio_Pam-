--1 - Selecione o nome do produto e calcule o total vendido;
SELECT
PR.PRODUTO,
SUM(PR.PRECO_UNITARIO * PE.QTD_VENDIDA) AS TOTAL_VENDIDO
FROM PRODUTO PR
JOIN PEDIDO PE ON PE.SKU = PR.codigo
GROUP BY PR.PRODUTO

--2 - Selecione o gênero do representante e calcule o total vendido;
SELECT
RE.GENERO,
SUM(PR.PRECO_UNITARIO * PE.QTD_VENDIDA) AS TOTAL_VENDIDO
FROM REPRESENTANTE RE
JOIN PEDIDO PE ON PE.MATRICULA = RE.ID_REP
JOIN PRODUTO PR ON PR.CODIGO = PE.SKU
GROUP BY RE.GENERO

--3 - Selecione a localização da loja, conte o número de pedidos que ocorreram em cada loja e calcule o total vendido;
SELECT
PE.LOJA,
COUNT(PE.PEDIDO) AS NUM_PEDIDOS,
SUM(PR.PRECO_UNITARIO * PE.QTD_VENDIDA) AS TOTAL_VENDIDO
FROM PRODUTO PR
JOIN PEDIDO PE ON PE.SKU = PR.CODIGO
GROUP BY PE.LOJA

--4 - Selecione o pedido, data do pedido, nome do produto, quantidade vendida, valor total da venda e nome completo do representante;
SELECT
PE.PEDIDO,
PE.DATA,
PR.PRODUTO,
PE.QTD_VENDIDA,
PE.QTD_VENDIDA * PR.PRECO_UNITARIO AS TOTAL_VENDIDO,
CONCAT(RE.NOME, ' ', RE.SOBRENOME) AS NOME_REPRESENTANTE
FROM PRODUTO PR
JOIN PEDIDO PE ON PE.SKU = PR.CODIGO
JOIN REPRESENTANTE RE ON RE.ID_REP = PE.MATRICULA
