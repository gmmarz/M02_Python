#Para criar um conjuto, é apenas passar os valores
set_frutas = {'banana','maça','uva'}
print(set_frutas)
#Um conjuto ele não é ordenado , e não possui index 
#Mas para grande volume de dados, ele acaba sendo mais otimizado para a procura.
#Adicionar um elemento ao conjunto.
set_frutas.add('Melão')
print(set_frutas)
#Para remover um elemento do set
set_frutas.remove('maça') #Caso não encontrado o valor dará um erro no programa
print(set_frutas)
set_frutas.add('maça')
print(set_frutas)
set_frutas.discard('maça')
print(set_frutas)