# 1.Crie uma função para calcular o IMC de 4 pessoas. Em seguida crie um programa que
# peça o peso e a altura de uma pessoa e implemente a função em seu
# programa.
# Atenção:
# Use as seguintes estruturas:
# -laço de repetição.
# -listas
# IMC = peso / altura ** 2

def calcular_imc(peso: float, altura:float):
    imc = peso/ altura ** 2
    return imc


print('Programa calculo IMC')

lst_pessoas = []
pessoa = {}

print('Coleta de informação')
for i in range(1,3 + 1):
    pessoa = {'nome':'','peso':0.0,'altura':0.0,'imc':0.0}
    pessoa['nome'] = input(f'Digite o nome da {i}º pessoa: ')
    pessoa['peso'] = float(input('Digite o peso: '))
    pessoa['altura'] = float(input('Digite sua altura: '))
    pessoa['imc'] = float(round(calcular_imc(pessoa['peso'],pessoa['altura']),2))

    lst_pessoas.append(pessoa)

#Mostrando informações
i = 1
for pessoa in lst_pessoas:
    pessoa_inf = pessoa.items()
    print(f'Informação pessoa {i}º pessoa: ')
    for inf in pessoa_inf:
        print(f'{inf[0]}: {inf[1]}')
    i +=1
 
