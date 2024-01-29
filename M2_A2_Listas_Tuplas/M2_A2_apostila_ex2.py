# 2. Dada a tupla de nomes de países: ("Brasil", "Canadá", "Austrália", "Espanha", "Índia"), crie um
# programa que itere sobre a tupla e exiba na tela cada país seguido pelo número de
# caracteres presentes em seu nome.
tupla_pais = ('Brasil','Canada','Austrália','Espanha','India')
for pais in tupla_pais:
    print(f'Pias: {pais}, letras: {len(pais)}')

print(f'Segunda opção: Pais e letra {[x + " tem " + str(len(x)) +" letras" for x in tupla_pais]}')   
    