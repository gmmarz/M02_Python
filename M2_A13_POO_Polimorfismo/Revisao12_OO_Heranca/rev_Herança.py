class Animal:
    def __init__(self, nome:str, idade:int) -> None:
        self.nome = nome
        self.idade = idade

    def fazer_barulho(self) -> None:
        print("Animal fazendo barulho")


class Cachorro(Animal):
    def __init__(self, nome: str, idade: int,raca : str) -> None:
        super().__init__(nome, idade)
        self.raca = raca
    
    def fazer_barulho(self) -> None:
        print("AUAU!") 
    
    def brincar(self) -> None:
        print(f'O Cachorro {self.nome}, está brincando')

class Gato(Animal):
    def __init__(self, nome: str, idade: int,cor:str) -> None:
        super().__init__(nome, idade)
        self.cor = cor

    def fazer_barulho(self) -> None:
        print("Miau!") 

    def dormir(self) -> None:
        print(f'{self.nome}: zzzzzzzzzzzzz')


dog1 = Cachorro("bob",8,"Vira lata")
cat1 = Gato("Mingual",8,"Caramelho")

cat1.dormir()