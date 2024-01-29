class Animal:
    def emitir_som(self) -> None:
        pass

class Cachorro(Animal):
    def emitir_som(self) -> str:
        # print("Cachorro fazendo: woof")
        return "Au au"

class Gato(Animal):
    def emitir_som(self) -> str:
        # print("Gato fazendo: meow!")
        return "miau"

class Passaro(Animal):
    def emitir_som(self) -> None:
        # print("Passro fazendo: piu")
        return "quiqui ui"

def fazer_som(Animal:Animal):
    print(Animal.emitir_som())

dog1 = Cachorro()
cat1 = Gato()
bird1 = Passaro()
dog2 = Cachorro()
cat2 = Gato()

animais = [dog1,cat1,bird1,dog2,cat2]

for animal in animais:
    fazer_som(animal)




