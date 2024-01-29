#Dicionário - estrutura com chaves e valores.

pessoa = {'nome':'Gui','idade':100}

# #Comando list() - retorna uma lista com as chaves do dicionario
# #        dic_name[nome] - retorna o valor referente ao identificador nome.

# print(list(dic_name))

#Para criar uma chave nova:
pessoa['email'] = 'test@gmail.com'
print(pessoa)

#Deletando uma chave
pessoa['wrongkey'] = 'teste'
print(pessoa)
del(pessoa['wrongkey'])
print(pessoa)

#Retorna o valor de uma chave especifica, ou o valor padrão caso a chave não exista.
print(pessoa.get('worngkey',-1))


