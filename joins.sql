use BDjoin

select * from Aluno
select * from Nota

-- inner join ou join

select aluno.id_aluno, aluno.nome, nota.nota
from aluno
inner join nota on aluno.id_aluno = nota.id_aluno;

-- segunda forma - inner join ou join

select a.id_aluno, a.nome, n.nota
from aluno a
inner join nota n on a.id_aluno = n.id_aluno;

--left join

select 
a.id_aluno,
a.nome,
n.nota
from aluno a
left join nota n on a.id_aluno = n.id_aluno;


--right join

select 
a.id_aluno,
a.nome,
n.nota
from aluno a
right join nota n on a.id_aluno = n.id_aluno;

--full outer join -- "a função de direita"

select 
a.id_aluno,
a.nome,
n.nota
from aluno a
full outer join nota n on a.id_aluno = n.id_aluno;


--cross join -- "a função de esquerda"

select 
a.id_aluno,
a.nome,
n.nota
from aluno a
cross join nota n 
order by Nome