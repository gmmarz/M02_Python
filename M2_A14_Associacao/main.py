"""
    Crie um sistema de escola
    Pessoa
    -nome
    -cpf(privado)
    Aluno(Pessoa)
    -endereco
    -nota
    Professor(Pessoa)
    -especialidade

    Turma
    Numero_turma(protegida)
    Curso
"""




from app_class import Pessoa, Aluno, Professor, Turma

prof1 = Professor('Joao','111.111.111-12','Matematica')
a1 = Aluno('pedro','222.222.222-21','paraiso',8)
a2 = Aluno('dani','333.333.333-31','sagrada familia',10)

print('-'*30)
print('Mostrnado as instancias das classes')
print(prof1.__dict__)
print(a1.__dict__)
print(a2.__dict__)

alunos = [a1,a2]

print('-'*30)
print('Mostrando informações turma')
t1 = Turma('2019','dec full stack',prof1,alunos)

print(t1)