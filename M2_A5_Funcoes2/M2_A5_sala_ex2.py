concatenar_string = lambda tx1,tx2: tx1+tx2 if len(tx1)>5 and len(tx2)>5 else 'Erro: Palavras devem ter mais de 5 caracter'

palavra1 = input('Digite a primeira palavra: ')
palavra2 = input('Digite a segunta palavra: ')

result = concatenar_string(palavra1,palavra2)

print(result)

print(concatenar_string('Casa', 'Maca'))