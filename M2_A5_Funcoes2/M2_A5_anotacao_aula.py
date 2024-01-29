#Revisão função 1
#Argumento nomeado é quando se chama uma função e passa o argumento indicando o valor que ele irá receber.
#Exemplo na sala criar uma função que retorna uma string invertida

# #Minha solução
# def inverter_string(text:str)->str:
#     i = len(text) - 1
#     nw_tx = ''
#     for _ in text:
#         nw_tx = nw_tx + text[i]
#         i -= 1
#     return nw_tx

# text = 'exemplo'
# nw_text = inverter_string(text)

# #Utilizando o slice para simplificar a função
# def inverter_palavra(palavra:str)->str:
#     return palavra[::-1]

# nw_palavra = inverter_palavra('exemplo')
# print(nw_palavra)
#--------------------------------------------------

# #Recebe dois numeros e retona o maior deles
# def Mostrar_maior_numero(lst_num:float)->float:
#     return max(lst_num)

# lst_num = [] 

# lst_num.append(float(input('Digite o primeiro numero: ')))
# lst_num.append(float(input('Digite o segundo numero: ')))

# maior_valor = Mostrar_maior_numero(lst_num)
# print(maior_valor)

#EXERCICIO 2 SEGUNDA SOLUÇÃO

# #Outra maneira de fazer 
# def maior_numero(num1,num2):
#     if num1 > num2:
#         return num1
#     else:
#         return num2

# nw_num1 = float(input('Digite o primeiro numero: '))
# nw_num2 = float(input('Digite o segundo numero: '))        

# maior =  maior_numero(nw_num1,nw_num2)
# print(maior)
# #---------------------------------------------------------------

# #Função recebe lista de palavras e retorna a mais longa: 

# def verifica_maior_palavra(lst_palavras):
#     maior_tamanho = 0
#     maior_palavra = ''
#     for palavra in lst_palavras:
#         tamanho = len(palavra)
#         if tamanho > maior_tamanho:
#             maior_palavra = palavra
#             maior_tamanho = tamanho
#     return maior_palavra

# lst_palavras = ['texto1','palavra2', 'pequena', 'grande','não']          

# maior_palavra = verifica_maior_palavra(lst_palavras)

# print(maior_palavra)
#--------------------------------------------------------------------

# #IMPRIMIR SEQUENCIA DE CORES
# cores = ['\033[44m','azul',
# '\033[0;0m',
#  '\033[42m','verde',
# '\033[0;0m',
#  '\033[43m','amarelo',
# '\033[0;0m']


# # print(cores[0] + cores[1] + cores[2])
# # print(cores[3] + cores[4] + cores[5])
# i = 0
# str_cor = ''
# for cor in cores:
#     str_cor = str_cor + cor
#     i += 1
#     if i == 2:
#         print(str_cor)
#         i=0
#         str_cor = ''

