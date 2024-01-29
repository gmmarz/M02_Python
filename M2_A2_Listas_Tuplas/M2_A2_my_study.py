# #Arquivo com meus estudos.
# lst_nomes = ['Maria','Antonia','Antonio']
# lst_nomes.insert(2,'jose')
# print(lst_nomes)

# #Metodo remove
# #Remove a primera ocorrencia da lista
# lst_nomes = ['Maria','Antonia','Antonio']
# print(lst_nomes)
# question = input('Qual nome você deseja remover da lista: ')
# lst_nomes.remove(question)
# print(lst_nomes)

from email_validator import validate_email,EmailNotValidError

flg = True

while flg:
    email = input("Digite seu email: ")

    try:
        chck_mail = validate_email(email).email
        flg = False
        break
    except EmailNotValidError as e:
        print('Email inválido')
        flg = True
   

print('Fim do programa')