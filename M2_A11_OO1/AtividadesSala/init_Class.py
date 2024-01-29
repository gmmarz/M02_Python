class Animal:
    def __init__(self,nome,idade, som):
        self.nome = nome
        self.idade = idade
        self.som = som
    def fazer_som(self):
        print(self.som)

animal1 = Animal("bob",3,"Au au")
animal2 = Animal("jubileu",2,"voce nao sabe nem eu")
print(animal1.nome)
print(animal2.nome)

animal1.fazer_som()

animal1.fazer_som

