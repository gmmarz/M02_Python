# #Criar tres dicionários com informações de aulos - nome, idade , e curso

# aluno1 = {'nome': 'gui', 'idade':'40', 'curso':'fullstack'}
# aluno2 = {'nome': 'Bi', 'idade':'39', 'curso':'biologia'}
# aluno3 = {'nome': 'leo', 'idade':'20', 'curso':'fisica'}


# lst_alunos = [aluno1,aluno2,aluno3]

# for aluno in lst_alunos:
#     print(aluno)

#Para criar a lista de forma dinamica:

lista_alunos = []
for _ in range(3):
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    curso = input('Digite seu curso: ')
    aluno = {'nome':nome,'idade':idade,'curso':curso}
    lista_alunos.append(aluno)
print(lista_alunos)