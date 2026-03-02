USE BDEscola

select *from aluno
select * from curso

-- tentativa 1

select 
a.nome_aluno,
a.id_aluno,
m.id_matricula,
m.id_aluno,
c.nome_curso
from aluno a 
inner join matricula m on a.id_aluno = m.id_aluno
inner join curso c on c.id_curso = m.id_curso