#Leia 4 notas de um aluno, calcule sua média, armazene em um dicionário as seguintes informações:
#a = Nome b=as 4 notas, c - maior nota , d- menor nota , e - media, f-situação

print('Programa de nota')
aluno_status = {'nome':'', 'notas': [], 'maior':0,'menor':0,'media':0,'situacao':''}

aluno_status['nome'] = input('Digite o nome do aluno: ')

lst_notas = []
for i in range(1,4+1):
    nota = float(input(f'Digite a {i}º nota: '))
    lst_notas.append(nota)
aluno_status['notas'] = lst_notas
aluno_status['maior'] = max(lst_notas)
aluno_status['menor'] = min(lst_notas)
aluno_status['media'] = sum(lst_notas)/len(lst_notas)
if aluno_status['media'] >=6 and aluno_status['media'] <=10:
    aluno_status['situacao'] = 'Aprovado'
elif aluno_status['media'] >=0  and aluno_status['media'] < 6:
    aluno_status['situacao'] = 'Reprovado'
else:
    aluno_status['situacao'] = 'Situação invalida, verifique o cadastro das notas'
# if aluno_status['media'] >= 6:
#     aluno_status['situacao'] = 'Aprovado'
# else:
#     aluno_status['situacao'] = 'Reprovado'
print('\n')
for _,(item,valor) in enumerate(aluno_status.items()):
    print(f'{item}:{valor}')


