class Cachorro:
    def __init__(self,nome, raca, idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade

    def __repr__(self) -> str:
        return f"Nome: {self.nome}, Raca: {self.raca}, Idade: {self.idade} "
    

dog1 = Cachorro("spock","caramelo",5)

print(dog1)
