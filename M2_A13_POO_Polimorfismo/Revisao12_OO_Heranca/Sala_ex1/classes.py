class Pessoa:
    def __init__(self,nome:str,idade:int,cpf:str) -> None:
        self.nome = nome
        self.__idade = idade
        self.__cpf = cpf
    
    @property
    def idade(self) -> int:
        return self.__idade

    @idade.setter
    def idade(self,nova_idade:int) ->None:
        if nova_idade > self.__idade:
            self.__idade = nova_idade
        else:
            print("Nova idade deve ser maior que idade atual")
    
    @property
    def cpf(self) -> str:
        return self.__cpf
    
#é possível acessar com o metodo super, mas não é incado, Neste caso melhor seguir com o atributo apenas privado com _cpf por exemplo.
class Funcionario(Pessoa):
    def __init__(self, nome: str, idade: int, cpf: str, cargo:str ) -> None:
        super().__init__(nome, idade, cpf)
        self.cargo = cargo
    
    def __repr__(self) -> str:
        return f'Nome: {self.nome} cpf : {super().cpf}'



if __name__ == "__main__":
    print("Este arquivo é um modulo e não deve ser executado")



