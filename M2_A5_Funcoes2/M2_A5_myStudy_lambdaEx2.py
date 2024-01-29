# 2. Implemente uma função lambda que receba duas strings e retorne a concatenação
# das duas, apenas se ambas as strings tiverem mais de 5 caracteres. Caso contrário,
# a função deve retornar uma mensagem de erro.

concatenar = lambda str1, str2: str1 + str2 if len(str1) >5 and len(str2) >5 else 'Error: Textos precisam ter mais que 5 caracteres'

txt1 = input("Digite o primeiro texto: ")
txt2 = input('Digite o segundo texto: ')

print(concatenar(txt1,txt2))