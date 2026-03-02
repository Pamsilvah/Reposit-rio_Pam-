-- FALAREMOS DE PROCEDURE
-- CRIAR PROCEDURE QUE LISTA TODOS OS PEDIDOS

create procedure sp_lista_pedidos

as
begin
select * from pedido
end;


-- executar procedure

exec sp_lista_pedidos

--alterar procedure

alter procedure sp_lista_pedidos
as
begin
select * from pedido
where sku = 'hl1918'
end;


------

-- procedure definindo variável -- buscar pedidos por sku

create procedure sp_busca_codigo -- definindo nome da procedure
@sku_produto varchar(50) -- defindo o parametro e o tipo de dado de busca
as 
begin -- limita o inicio de uma instrução
select * from pedido -- seleciona todas as buscas da tabela pedido
where sku = @sku_produto -- adiciona um filtro na sua coluna sku sendo igual ao valor variável
end; -- limita o fim de uma instrução


-- execução procedure com parametro/variavel

exec sp_busca_codigo 'hl1918'



-------------------------------------

-- 1- procedure: sp_vendas - que exiba todas as tabelas e pedidos
-- o valor pode ser atribuido , ou seja o msm que dizer que ele é uma variavel (X) -- <<PRA MIM RODA ASSIM RSRRS>>

create procedure x_vendas-- definindo nome da procedure
@x_vendas varchar(50) -- defindo o parametro e o tipo de dado de busca
as 
begin -- limita o inicio de uma instrução
select * from pedido -- seleciona todas as buscas da tabela pedido
where sku = @x_vendas -- adiciona um filtro na sua coluna sku sendo igual ao valor variável
end; -- limita o fim de uma instrução

exec x_vendas 'hl1918'


-----------------------------------------

-- 2- procedure: sp_produtos - que exiba > tds colunas da tabela produto, filtrando pelo codigo do produto.

create procedure sp_produtos -- estou def. o nome da procedure
@X_produtos varchar(50)     -- def. um parametro e o tipo de dado
as
begin						 --limita o inicio de uma instrução
select * from produto
where  codigo = @X_produtos  -- procurando um produto "X" FILTRO
end;						-- limita o fim de uma instrução

exec sp_produtos 'hl1918'  -- aqui estou filtrando o produto pelo seu codigo // EXIBINDO


---------------------------------------

-- 3- procedure: sp_genero_representantes que exiba 

create procedure sp_genero_representantes
@X_generos varchar(50)
as
begin
select * from representante 
where genero = @x_generos -- filtrando o meu dado > genero
end;

exec sp_genero_representantes 'm'



-- 4- procedure: sp_vendas_produtos - produto, qtd total, o valor total vendido, filtrando pelo nome do produto.

