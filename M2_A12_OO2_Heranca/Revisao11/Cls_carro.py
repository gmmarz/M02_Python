class Carro:
    #Fazendo dessa forma os atributos são fixos nos objetos.
    # cor = "vermelho"
    # qnt_portas = 4
    # marca = "BMW"

    def __init__(self,cor: str,marca: str,qnt_portas: int = 4) -> None:
        self.cor = cor
        self.qnt_portas = qnt_portas
        self.marca = marca

    def __repr__(self) -> str:
        return f"Cor: {self.cor}, Quantidade de portas: {self.qnt_portas}, marca: {self.marca}"

    def acelerar(self):
        print("Acelerando")


if __name__ == "__main__":
    print("Este é um modulo")
