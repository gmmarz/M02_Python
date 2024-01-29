#Para deixar o atributo privado de verdade
# definir um atributo com dois __saldo por exemplo.
# Com isso ele não pode ser acessado diratamente e nem escrito.

class Conta:
    def __init__(self,nome) -> None:
        self._nome = nome
        self.__saldo = 0

    @property
    def saldo(self) -> float:
        return self.__saldo
    
    @saldo.setter
    def saldo(self,novo_saldo:float):
        if novo_saldo >= 0:
            self.__saldo = novo_saldo
        else:
            print("Valor passado nao pode ser menor que zero")
        

conta1 = Conta("Not")
conta1.__saldo
print(conta1.saldo)
conta1.saldo = 123
print(conta1.saldo)
conta1.saldo = -123
print(conta1.saldo)







