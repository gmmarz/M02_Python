#Programa que vai pedir 4 nomes e adicionar em uma lista no final mostrar a lista
lst_nome = []

# for i in range(4):
#     lst_nome.append(input('Digite um nome: '))

# print(f'A lista salva foi {lst_nome}')

#Resposta do professor:
# Como não vamos utilizar o a iteração pode-se criar o for com o _
for _ in range(4):
    nome = input('Digite um nome: ')
    lst_nome.append(nome)
print(f'A lista salva foi {lst_nome}')