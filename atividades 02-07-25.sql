-- Criação das tabelas 





-- Aluno 
create table aluno(
id_aluno int not null,
nome_aluno varchar(50) not null,
data_nascimento date not null,
telefone varchar(11));


--Matricula 
create table matricula(
id_matricula int not null,
id_aluno int not null,
id_curso int not null,
data_inicio date not null,
data_fim date not null);





--Curso
create table curso(
id_curso int not null,
nome_curso varchar(30),
carga_horaria int); 



-- Seleção nas Tabelas
Select * from aluno;
Select * from matricula;
Select * from curso;

--Inserção de dados
--Curso
Insert into curso(id_curso,nome_curso,carga_horaria)
values
(1, 'Banco de Dados', 80),
(2, 'Desenvolvimento Web', 100),
(3, 'Redes de Computadores', 90),
(4, 'Análise de Daods',120),
(5,  'Segurança da Informação',110);


--Inserção de Dados
-- Aluno
INSERT INTO ALUNO (ID_Aluno, Nome_aluno, Data_nascimento, Telefone) 
VALUES
(1, 'Larissa Martins', '1998-03-12', '11983452178'),
(2, 'Thiago Souza', '1989-07-29', '21997635490'),
(3, 'Camila Fernandes', '2001-11-04', '31987654321'),
(4, 'Diego Henrique', '1997-02-15', '41999086721'),
(5, 'Juliana Rocha', '1985-06-23', '51996478802');


-- Matrícula

INSERT INTO MATRICULA (ID_Matricula, ID_Aluno, ID_Curso, Data_Inicio, Data_Fim)
VALUES
(1, 1, 4, '2024-03-01', '2024-06-30'),
(2, 2, 2, '2024-03-15', '2024-07-15'),
(3, 3, 3, '2024-02-20', '2024-06-20'),
(4, 4, 1, '2024-04-05', '2024-08-05'),
(5, 5, 2, '2026-01-10', '2024-05-10'),
(6, 3, 1, '2026-07-01', '2024-10-31');

-- Apagar dados da tabela
Truncate table Aluno;
Select * from ALuno; 

Truncate table Matricula;
Select * from Matricula;

Truncate table Curso;
Select * from Curso;






