#ex16 - fazer um dicionário frutas
frutas = {}
#ex17 - adicionar frutas
frutas.update({"maca":10,"pera":5,"uva":15})

#ex18 - imprimir o valor de uma chave
print(frutas.get("banana","A fruta não existe"))

#ex19 - verificar se a chave banana existe caso não criar e em seguinda incrementar
if "banana"  not in frutas:
    frutas["banana"] = 5
frutas["banana"] = frutas["banana"] + 1

#x20 verificar se frutas está vazio
if len(frutas)==0:
    print("Dicionario está vazio")
else:
    print("Dicionario tem informações")