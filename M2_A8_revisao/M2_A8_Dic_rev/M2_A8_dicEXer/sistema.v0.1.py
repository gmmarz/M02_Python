itens=['celular','batedeira','televisao','notebook','aparelho_dvd']
valores = [1000.0,350.0,3450.0,6700.0,200.0]

produtos = {itens[x]:valores[x] for x in range(0,len(itens)) }

# print(produtos)
prod = input("Digite um produto: ")

# if prod in 