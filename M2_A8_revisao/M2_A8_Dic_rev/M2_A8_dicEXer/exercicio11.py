#Ex11 
estoque = {"item1":10,"item2":5,"item3":20}
#ex12 - retornar soma dos produtos

print(f"total = {sum( estoque.values())}")

#ex13 verificar item2
print("item2" in estoque)

#ex14 removendo item3 
estoque.pop("item3")

#ex15 criando um novo item
estoque.update({"item25": 15})
