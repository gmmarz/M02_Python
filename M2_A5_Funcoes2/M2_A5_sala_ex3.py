#Funcao que retorna numero se ele for maior que 10 se não for retorna o numero/2
verificar_num = lambda num: num if num > 10 else num/2

num = float(input('Digite um número: '))

result = verificar_num(num)

print(result)
