# 3. Escreva uma função lambda que receba um número e verifique se ele é maior que 10.
# Se for maior, a função deve retornar o próprio número; caso contrário, deve retornar o
# número dividido por 2.

verificar_numero = lambda x : x if x > 10 else x/2

print(verificar_numero(float(input('Digite um número: '))))