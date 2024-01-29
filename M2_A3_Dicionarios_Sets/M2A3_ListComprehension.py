# #Criar a list comprehension , crie uma lista a partir de uma tupla de numeros com os valores ao quadrado.
# num_tupla = (1,2,3,4,5,6,7,8)

# lst_num = [num**2 for num in num_tupla]
# print(lst_num)

#Ex6 Criar uma variável e guardem dentro dela um texto.
#criar uma lista apenas com as vogais desta frase, utilizando o list comprehensio

frase = "Hoje estou na aula 2 de programaçao em Python"

lst_vogais = [letra for letra in frase if letra in ('a','e','i','o','u')]

print(lst_vogais)
