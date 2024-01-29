#Enunciado
# 4.Crie Funções para calcular de acordo com os operadores matemáticos de uma
# calculadora:
# ●somar(parm1, parm2)
# ●subtracao(parm1, parm2)
# ●multiplicacao(parm1, parm2)
# ●divisao(parm1, parm2)

# Em seguida, escreva um programa que receba dois números inteiros ou float e que
# possa calcular esses números de acordo com a escolha dos usuários sob operadores.

# Use um laço de repetição infinito e verifique a cada resultado da operação selecionada se o
# usuário deseja continuar calculando, se não, interrompa o loop e finalize o programa.
# use bloco condicional para chamar a função apropriada
# crie comentarios em seus códigos
# utilize type hint
# a função de divisão deverá informar ao usuário uma mensagem de erro se o divisor for igual a
# zero

def somar(param1:int|float,param2:int|float)->int|float:
    resultado = param1 + param2
    return resultado

def subtrair(param1:int|float,param2:int|float)->int|float:
    resultado = param1 - param2
    return resultado

def multiplicar(param1:int|float,param2:int|float)->int|float:
    resultado = param1 * param2
    return resultado

def dividir(param1:int|float,param2:int|float):
    if param2 == 0:
        resultado = 'Não é possível divisão por 0'
    else:
        resultado = round(param1/param2,2)
    return resultado

print('Programa para calcular dois numeros')

while True:
    resultado = ''
    oper = ''
    print('Escolha uma das operações:\n1-Soma\n2-Subtração\n3-multiplicação\n4-Divisão\n0-Sair')
    try:
        escolha=int(input('Digite sua opção: '))
    except ValueError:
        print('Digiete apenas as opções indicadas')
    if escolha == 0:
        break
    else:
        try:
            num1 = float(input('Digite o primeiro número: '))
            num2 = float(input('Digite o segundo número: '))
        except ValueError:
            print('Digite apenas valores númericos')
        match escolha:
            case 1:
                resultado = somar(num1,num2)
                oper = '+'
            case 2:
                resultado = subtrair(num1,num2)
                oper = '-'
            case 3:
                resultado = multiplicar(num1,num2)
                oper = '*'
            case 4:
                resultado = dividir(num1,num2)
                oper = '/'
            case 0:
                break
        print('----------------------------------------------\n')
        print(f'O resultado {num1} {oper} {num2} = {resultado} ')
        print('----------------------------------------------\n')
    

        
        

                



