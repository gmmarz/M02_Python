# 3. Você recebeu uma lista de tuplas, onde cada tupla contém o nome de um produto e seu
# preço. Por exemplo: [("Maçã", 2.50), ("Banana", 1.75), ("Laranja", 3.00)]. Escreva um programa
# que itere sobre essa lista e calcule o valor total dos produtos, exibindo-os na tela.
lst_items = [("Maçã", 2.50), ("Banana", 1.75), ("Laranja", 3.00)]
#Utilizando lista comprehension para pegar os valores dos itens
lst_valor = [val[1] for val in lst_items]        #para boas praticas quanto são duas funções utiliza-se separado.
print(f'O total dos itens é: {sum(lst_valor)}')  #Este exemplo seria o melhor.

print('--------------------------------------')
print('Segundo exemplo com comprehension')

print(f'Falor total dos itens: {sum([val[1] for val in lst_items])}') #Neste caso ficaria um pouco mais complicado
                                                                      #de interpretar pois está fazendo duas funções juntas
                                                                      

