from cls_forma import (Forma,Retangulo,Circulo)

def calcular_area(figura:Forma) -> float:
    return figura.calcular_area()
def calcular_perimetro(figura:Forma) -> float:
    return figura.calcular_perimetro()


ret = Retangulo(20,15)
circ = Circulo(20)

print(f'Area do retangulo é: {calcular_area(ret)}')
print(f'Perimetro do retangulo é: {calcular_perimetro(ret)}')

print(f'Area do circulo é: {calcular_area(circ)}')
print(f'Perimetro do circulo é: {calcular_perimetro(circ)}')
