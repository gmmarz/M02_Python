class Pessoa:
    def __init__(self, nome: str, idade:int, cpf: str, status: str = "Parado") -> None:
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.status = status

    def andar(self):
        self.status = "Andando"
        self.mostrar_status()
    
    def correr(self):
        self.status = "Correndo"
        self.mostrar_status()

    def mostrar_status(self):
        print(f"O {self.nome} está {self.status}")

    def parar(self):
        self.status = "parado"
        self.mostrar_status()

    def __repr__(self) -> str:
        return f"Nome: {self.nome}, Idade: {self.idade}, cpf: {self.cpf}, status: {self.status}"