# class Veiculo:

#     def __init__(self, marca, modelo):

#         self.marca = marca

#         self.modelo = modelo



#     def ligar_motor(self):

#         return "Motor ligado"



# class Carro(Veiculo):

#     def __init__(self, marca, modelo, num_portas):

#         super().__init__(marca, modelo)

#         self.num_portas = num_portas



#     def ligar_motor(self):

#         return f"{self.marca} {self.modelo} motor ligado"



# class CarroEletrico(Carro):

#     def __init__(self, marca, modelo, num_portas, capacidade_bateria):

#         super().__init__(marca, modelo, num_portas)

#         self.capacidade_bateria = capacidade_bateria



#     def ligar_motor(self):

#         return "Carros elétricos não possuem motor tradicional. Pressione o botão de ligar."



# # Teste de código

# carro_eletrico = CarroEletrico("Tesla", "Model S", 4, "100 kWh")

# print(carro_eletrico.ligar_motor())

# [PY-A12] Considere as seguintes classes em Python:

class Animal:

    def __init__(self, name):

        self.name = name



    def speak(self):

        return "O animal faz barulho."





class Dog(Animal):

    def __init__(self, name, breed):

        super().__init__(name)

        self.breed = breed



    def speak(self):

        return "O cachorro late."





class Cat(Animal):

    def __init__(self, name, color):

        super().__init__(name)

        self.color = color



    def speak(self):

        return "O gato mia."



# Qual é o resultado da execução do seguinte código?



dog = Dog("Rex", "Labrador")

print(dog.name)