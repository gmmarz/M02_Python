class Conta:
    def __init__(self, nome:str, telefone_contato:str, cpf:str) -> None:
        self.nome = nome
        self.telefone_contato = telefone_contato
        self._cpf = cpf
        self.__saldo = 0

    @property
    def cpf(self) -> str:
        return self._cpf
    
    @property
    def saldo(self)-> float:
        return self.__saldo
    
    def deposito(self,valor:float) -> None:
        self.__saldo = self.__saldo + valor
    
    def saque(self, valor: float) -> None:
        self.__saldo = self.__saldo - valor

    def __repr__(self) -> str:
        pass

if __name__ == "__main__":
    print("Este é um modulo nao deve ser executado")