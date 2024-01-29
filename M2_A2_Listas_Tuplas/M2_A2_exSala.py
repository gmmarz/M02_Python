# #Dicas de listas 
# # Apesar da lista poder ter cada membro de uma tipo de variável. 
# # é usual para ficar mais coerente que cada lista seja de apenas um tipo. 
# lst_compras = ['arroz','feijao','oleo','acucar']

# # #Exemplo de uma maniera de ler e salvar os membros em variáveis(Descompactando)
# # (item1,item2,item3,item4) = lst_compras
# # print(f'1 -{item1}\n2-{item2}\n3-{item3}\n4-{item4}')

# #metodos slice da lista - para poder ler pedaços da lista 
# print(lst_compras[1:4:2]) # irá começar da posição 1 e dando um passo de 2. irá mostrar feijao e acucar

#METODOS DE MANIPULAÇÂO DA LISTA
#append - adiciona um item no ultimo lugar da lista

#insert - adiciona um item no lugar indicado da lista  
# lst_compras.insert(0,'alface') # irá inserir alface no começo

#pop - Para remover um item da lista
# lst_compras.pop() #Remove o ultimo valor da lista e retorna o valor.
# lst_compras.pop(2)#Remove o item da posição 2.
# valor_removido = lst_compras.pop(2)
# print(f'Valor removido foi {valor_removido}')

#Sort - Organiza a lista de forma crescente ou alfabetica
# print(lst_compras.sort()) # Precise ser uma lista do mesmo tipo.
# lst_compras = ['arroz','feijao','oleo','acucar']
# print(lst_compras)

# #Count - Conta quantas ocorrencias existe de um item
# lst_compras = ['arroz','acucar','feijao','oleo','acucar']
# print(lst_compras)
# lst_compras.sort()
# print(lst_compras)
# print(lst_compras.count('acucar'))

#Para listas numericas
# sum(lst_num) - soma dos valores
# max(lst_num) - valor maximo
# mean(lst_num) - valor médio

#Metodo list() - cria uma lista. Pode ser usado para criar uma lista a partir de uma lista
# tupla_frutas = ('maça','abacate','pera','uva')
# lst_frutas = list(tupla_frutas) #cria uma lista de frutas com os valores da tupla_frutas. A tupla uma vez criada não 
# #pode ser modificada.
# #Uma tupla pode ser criar com comprehension

# #DICA DE DESCOMPACTAMENTO
# tupla_frutas = ('maça','abacate','pera','uva')
# (fruta1,fruta2,*outras_frutas) = tupla_frutas  #O *outras_frutas salvara o resto das frutas em uma lista
# print(f'fruta1: {fruta1}, fruta2: {fruta2} e o resto: {outras_frutas}')

