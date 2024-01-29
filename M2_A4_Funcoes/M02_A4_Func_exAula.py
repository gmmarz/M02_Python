#Fazer um programa que irá calcular o IMC de uma pessoa e imprir o IMC

#Quando adicionado o tipa da variável na frente, isso fará que ao chamar a função apareça dicas sobre o que
#a função espera receber. Porem não dará erro caso a função receba uma string ou algum tipo diferente.
def imprime_menu():
    print('-'*30)
    print('Menu')
    print('-'*30)

def calcular_IMC(peso:float|int, altura:float|int)->float:
    imc = round(peso/altura**2,2)
    return imc


print('Programa para calcular o IMC')

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

result_imc = calcular_IMC(peso,altura)
imprime_menu()
print(f'O seu IMC = {result_imc}')



