# EX-Apostila:  Leia os dados de um usuário - nome, sobrenome, idade, email - e
#  imprima-os enumerando os mesmos

# flg_data = True

dic_usuário = dict([('nome',''),('sobrenome',''),('idade',0),('email','')])

# while flg_data:
print('Cadastro novo usuário, digite as informações: ')
dic_usuário['nome'] = input('Nome: ')
dic_usuário['sobrenome'] = input('Sobrenome: ')
dic_usuário['idade'] = int(input('Idade como número inteiro: '))
dic_usuário['email'] = input('email: ')
print('\n')

if len(dic_usuário)>=1:
    for i, (item,valor) in enumerate(dic_usuário.items()):
        print(f'{i+ 1}-{item}:{valor}')
else:
    print("Programa finalizado sem nenhum cadastro realizado.")
        
