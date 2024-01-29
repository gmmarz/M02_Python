class Cachorro:
    def __init__(self,nome:str,raca:str,idade:int) -> None:
        self.nome = nome
        self.raca = raca
        self.idade = idade

    def mostrar_atributos(self):
        return {"nome": self.nome, "raca": self.raca,"idadde":self.idade}