class Animal:
    def fazerSom(self):
        pass

#Classe cachorro herda classe animal e implementa fazer som
class Cachorro(Animal):
    def fazerSom(self):
        return "Woof!"
#Classe gato heda classe animal e implementa fazer som
class Gato(Animal):
    def fazerSom(self):
        return "Meow!"
#Classe pato herda classe anumal e implementa fazer som
class Pato(Animal):
    def fazerSom(self):
        return "Quack!"
    
#Função do programa que usa o polimorfismo
def fazer_animal_falar(animal: Animal):
    return animal.fazerSom()


#Criando um animal de cada tipo e utilizando for para testar o polimorfismo
rex = Cachorro()
whiskers = Gato()
donald = Pato()

animais = [rex,whiskers,donald]

for animal in animais:
    print(animal.__class__.__name__,"faz", fazer_animal_falar(animal))