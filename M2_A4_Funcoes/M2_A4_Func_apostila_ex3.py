# 3.Crie uma função que calcule o valor/hora do funcionário, em seguida implemente
# essa função em um programa de calcular hora e valor do funcionário.
# Utilizando a formula do artigo 271 do código do trabalho
# preco_hora = (renda mensal * 12 meses/(52semanas * horas semanal))

def calcular_preco_hora(salario_mes:float, horas_semana:float):
    preco_hora = (salario_mes*12)/(52 * horas_semana)
    return preco_hora

print('Calculo do preco hora conforme artigo 271 código do trabalho')

while True:
    sal_mes = float(input('Digite salario mensal(digite -1 para encerrar): '))
    if sal_mes == -1:
        break
    else:
        horas_semanais =float(input("Digite as horas semanas: "))
    preco_hora = calcular_preco_hora(sal_mes,horas_semanais)

    print(f'\nO preço hora para o salario = {sal_mes} trabalhando {horas_semanais} por semana é de: {round(preco_hora,2)} por hora')

print("Programa finalizado pelo usuário")
