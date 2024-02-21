import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()
cursor.execute('PRAGMA foreign_key=ON')



#1. Crie uma tabela chamada "alunos" com os seguintes campos: id(inteiro), nome (texto), idade (inteiro) e curso (texto).
cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100));')

#2. Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.
cursor.execute('INSERT INTO alunos(id, nome,idade,curso) VALUES(1, "Dani", 30, "Medicina")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (2, "Luana", 20, "Enfermagem")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(3, "José", 25, "Engenharia")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(4, "Leo", 32, "Aurquitetura")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(5, "Suelen", 30, "Análise de Sistemas")')


#3. Consultas Básicas Escreva consultas SQL para realizar as seguintes tarefas: 
#a) Selecionar todos os registros da tabela "alunos".
dados = cursor.execute('SELECT * FROM alunos ')
for alunos in dados:
   print(alunos)

#b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
dados = cursor.execute('SELECT * FROM alunos WHERE idade > 20 ')
for alunos in dados:
   print(alunos)   

#c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
dados = cursor.execute('SELECT * FROM alunos WHERE curso = "Engenharia" ORDER BY nome ASC')
for alunos in dados:
   print(alunos) 

#d) Contar o número total de alunos na tabela
dados = cursor.execute('SELECT COUNT(*) FROM alunos')
for alunos in dados:
   print(alunos) 


#4. Atualização e Remoção
#a) Atualize a idade de um aluno específico na tabela.
cursor.execute('UPDATE alunos SET idade="22" WHERE nome="Dani"')

#b) Remova um aluno pelo seu ID.
cursor.execute('DELETE FROM alunos where id=5')


#5. Criar uma Tabela e Inserir Dados: Crie uma tabela chamada "clientes" com os campos: id (chaveprimária), nome (texto), idade (inteiro) e saldo (float). Insira alguns registros de clientes na tabela.

cursor.execute('CREATE TABLE clientes (id INT PRIMARY KEY,nome VARCHAR(100), idade INT,saldo FLOAT);')
cursor.execute('INSERT INTO clientes(id, nome,idade,saldo) VALUES(1, "Maria", 42, 3.02)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (2, "Julia", 25, 1000)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(3, "Ana", 32, 124.35)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(4, "Renan", 18, 23.47)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(5, "Angélica", 30, 35.98)')

#6. Consultas e Funções Agregadas: Escreva consultas SQL para realizar as seguintes tarefas:
#a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.
dados = cursor.execute('SELECT * FROM clientes WHERE idade > 30 ')
for clientes in dados:
   print(clientes) 

#b) Calcule o saldo médio dos clientes.
dados = cursor.execute('SELECT AVG(saldo) FROM clientes ')
for clientes in dados:
   print(clientes) 

#c) Encontre o cliente com o saldo máximo
dados = cursor.execute('SELECT * FROM clientes WHERE saldo = (SELECT MAX(saldo) FROM clientes)')
for clientes in dados:
   print(clientes)

#d) Conte quantos clientes têm saldo acima de 1000.
dados = cursor.execute('SELECT COUNT(*) FROM clientes WHERE saldo > 1000')
for clientes in dados:
   print(clientes)

#7. Atualização e Remoção com Condições
#a) Atualize o saldo de um cliente específico.
cursor.execute('UPDATE clientes SET saldo="2345" WHERE nome="Renan"')

#b) Remova um cliente pelo seu ID.
cursor.execute('DELETE FROM clientes where id=3')

#8. Junção de Tabelas
#Crie uma segunda tabela chamada "compras" com os campos: id (chave primária), cliente_id (chave estrangeira referenciando o id
#da tabela "clientes"), produto (texto) e valor (real). Insira algumas
#compras associadas a clientes existentes na tabela "clientes".
#Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.

cursor.execute(''' CREATE TABLE compras (id INTEGER PRIMARY KEY,cliente_id INTEGER,produto VARCHAR(100),valor REAL,FOREIGN KEY (cliente_id) REFERENCES clientes(id))''')
cursor.execute('INSERT INTO compras (id,cliente_id, produto, valor) VALUES (1, 5, "Batom", 22.50)')
cursor.execute('INSERT INTO compras (id,cliente_id, produto, valor) VALUES (2, 4, "Bolsa", 33.60)')
cursor.execute('INSERT INTO compras (id,cliente_id, produto, valor) VALUES (3, 3, "Blusa", 58)')
cursor.execute('INSERT INTO compras (id,cliente_id, produto, valor) VALUES (4, 2, "Calça", 100.65)')
cursor.execute('INSERT INTO compras (id,cliente_id, produto, valor) VALUES (5, 1, "Sapato", 280.69)')

dados = cursor.execute(' SELECT c.nome, co.produto, co.valor FROM clientes c JOIN compras co ON c.id = co.cliente_id;')
for clientes in dados:
   print(clientes)

conexao.commit()
conexao.close