#Aula de funções
#Quando for necessário passar alguma informação para a função, este valor é chamado de argumento da função.

# #Exemplo de um exemplo para saudar
# def saudar(nome):
#     print("Bem vindo")
#     print('Welcome')
#     print('Bien venue')

# nome = input('Digite seu nome: ')
# saudar(nome)
# frase = input('Digite uma frase: ')

#Dicas funções
#Nomeclatura - preferencialmente ter nomes verbais, que indicam bem o que a função está fazendo
#A função deve ter sua responsabilidade.
#Caso a validação dos dados esteja dentro da funcionalidade da função a validação pode ser feita na função

#Para passar um type hint basta escrever na frente da variável : e o tipo da variáveç
#Para passar uma dica sobre qual o tipo que a função irá retornar colocar na frente dela -> tipo variavel
#Variáveis que são iniciadas(opcionais) automaticamente mostrarão o type hint conforme sua inicialização

#Caso desejado um parametro opcional basta inicialo na definição da função
def somar(n1:int,n2=0,n3 =10)->int: #Mas quando 1 parametro é iniciado, todos depois desse também devem ser. n2 e n3 são parametros 
                           #opcionais.
    soma=n1 + n2 + n3
    return soma

resultado = somar(2,n3=10) #Este caso o n3 é um parametro nomeado



