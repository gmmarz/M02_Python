# Escreva uma função lambda que receba um número e verifique se ele é par ou
# ímpar. A função deve retornar "par" se o número for par e "ímpar" caso contrário.

verificar_par = lambda x : 'Número digitado é Par' if x%2 == 0 else 'número digitado é impar'

while True:
    str_num = input('digite um número ou ditie s para sair:  ')

    if str_num == 's':
        break
    else:
        try:
            num = int(str_num)
            print(verificar_par(num))
        except ValueError:
            print('Digite apenas números inteiros')
print('-'*30)
print('Programa finalizado')
