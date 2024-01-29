import math

class Forma:
    def __init__(self,altura:float, largura:float) -> None:
        self.altura = altura
        self.largura = largura

    def calcular_area(self):
        pass
    
    def calcular_perimetro(self):
        pass

class Circulo(Forma):
    def __init__(self, altura: float, largura: float) -> None:
        super().__init__(altura, largura)
        self.raio = largura/2

    def calcular_area(self) -> float:
        return math.pi * (self.raio ** 2)
    
    def calcular_perimetro(self):
        return (2 * math.pi) * self.raio
    
class Retangulo(Forma):
    def __init__(self, altura: float, largura: float) -> None:
        super().__init__(altura, largura)

    def calcular_area(self):
        return self.largura * self.altura
    
    def calcular_perimetro(self):
        return 2*(self.altura +self.largura)
    

circ = Circulo(0,20)
print(f"Area do circulo = {circ.calcular_area()}")
print(f"Perimetro do circulo = {circ.calcular_perimetro()}")

retangulo1 = Retangulo(5,10)
print(f"Area do retangulo = {retangulo1.calcular_area()}")
print(f"Perimetro do retangulo = {retangulo1.calcular_perimetro()}")
   


