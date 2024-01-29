# 4. Considere a seguinte lista de palavras: ["Python", "é", "uma", "linguagem", "poderosa"]. Escreva
# um programa que itere sobre essa lista e exiba apenas as palavras que possuem mais de 4
# letras.
lst_palavras = ["Python", "é", "uma", "linguagem", "poderosa"]
lst_mais_4_letras = [palavra for palavra in lst_palavras if len(palavra)>4]
print(lst_mais_4_letras)