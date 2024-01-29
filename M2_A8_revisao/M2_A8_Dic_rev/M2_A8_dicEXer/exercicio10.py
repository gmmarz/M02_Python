pessoas = {}

pessoas = {"nome":"joao"}

# #Ex3
# print(pessoas["nome"])

#ex4
pessoas.update({"idade":25,"cidade":"Belo Horizonte"})

#ex6-removendo chave do dicionário:
pessoas.pop("cidade")


#ex7-Alterar valor
pessoas['idade'] = 30

pessoas.update({"idade":40})

#ex10 Imprimindo todos os valores
print(pessoas.items())




