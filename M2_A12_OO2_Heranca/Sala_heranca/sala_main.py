#Herança criando a classe mae
class Animal:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    def fazer_barulho(self):
        print("Ta fazendo barulho")
    
class Cachorro(Animal):
    def __init__(self, nome: str, idade: int, raca: str) -> None:
        super().__init__(nome, idade)
        self.raca = raca

    def fazer_barulho(self):
        return "Está latindo"

class Gato(Animal):
    def __init__(self, nome: str, idade: int, cor: str) -> None:
        super().__init__(nome, idade)
        self.cor = cor
    def fazer_barulho(self):
        return "Está miando"
    
cachorro1 = Cachorro("Bob",5,"Pincher")
gato1 = Gato("Sushi", 3, "laranja")

cachorro1.fazer_barulho()
gato1.fazer_barulho()
