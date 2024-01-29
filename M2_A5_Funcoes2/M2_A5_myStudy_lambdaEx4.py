# 4. Implemente uma função lambda que receba um número e verifique se ele é divisível
# por 3 e por 5. A função deve retornar "divisível" se a condição for satisfeita e "não
# divisível" caso contrário.

verificar_divisivel = lambda x: "É divisivel por 3 e por 5" if x%3 == 0 and x%5 == 0 else 'Não é divisível'

print(verificar_divisivel(float(input('Digite um número: '))))