# 2.Crie uma função que retorne quantas letras possui uma palavra. Se for passado uma
# frase, a função deverá retornar o número de letras, espaços vazios e quantos sinais
# de pontuação.

def contar_letras(frase: str):
    lst_frase = frase.split(' ')
    cnt_pontuacao = 0
    cnt_letras = 0
    cnt_espaco = 0
    if len(lst_frase)>1:
        cnt_espaco = len(lst_frase)
        for caractere in frase:
            if caractere in ['.',',','!','?',';']:
                cnt_pontuacao +=1
            else:
                cnt_letras +=1
        result = {'letras': cnt_letras,'pontuacao':cnt_pontuacao,'espaco':cnt_espaco}
    else:
        for caractere in frase:
            cnt_letras +=1
        result ={'letras': cnt_letras}
    return result

frase = input('Digite uma palavra ou frase: ')
frase_inf = contar_letras(frase)
print('\nInformações sobre o texto digitado')
for inf in frase_inf.items():
    print(f'{inf[0]}: {inf[1]}')


