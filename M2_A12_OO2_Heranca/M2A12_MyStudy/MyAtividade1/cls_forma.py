class Forma:

    def calcular_area(self) ->float:
        pass
    
    def calcular_perimetro(self) -> float:
        pass

class Circulo(Forma):
    def __init__(self,raio) -> None:
        super().__init__()
        self.raio = raio
        self.pi = 3.145926535898
    def calcular_area(self):
        return self.pi*self.raio**2
    def calcular_perimetro(self):
        return 2*self.pi*self.raio
    
class Retangulo(Forma):
    def __init__(self,base,altura) -> None:
        self.base = base
        self.altura = altura
    def calcular_area(self) -> float:
        return self.base*self.altura
    def calcular_perimetro(self) -> float:
        return 2*(self.base + self.altura)

    
    