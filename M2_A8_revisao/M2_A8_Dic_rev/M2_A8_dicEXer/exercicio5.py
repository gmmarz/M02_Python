pessoas = {}

pessoas = {"nome":"joao"}

#Ex3
print(pessoas["nome"])

#ex4
pessoas.update({"idade":25,"cidade":"Belo Horizonte"})
print(pessoas)
#ex5
print("altura" in pessoas)

#ex6-removendo chave do dicionário:
pessoas.pop("cidade")

#ex7-Alterar valor
pessoas['idade'] = 30
print(pessoas)
pessoas.update({"idade":40})
print(pessoas)

#ex8 imprimindo todas as chaves do dicionário
for chave in pessoas:
    print(chave)
print(pessoas.keys())
#ex9 imprimindo todos os valores do dicionário
print('ex9')
for chave in pessoas:
    print(pessoas[chave])
pessoas.values()

