class Conta:
    def __init__(self, nome:str, telefone_contato:str) -> None:
        self.nome = nome
        self.telefone_contato = telefone_contato
    def __repr__(self) -> str:
        pass
    
class ContaJuridica(Conta):
    def __init__(self, nome: str, telefone_contato: str,cnpj:str) -> None:
        super().__init__(nome, telefone_contato)
        self.cnpj = cnpj
    
    def __repr__(self) -> str:
        return f'Nome: {self.nome}, Telefone: {self.telefone_contato}, CNPJ: {self.cnpj}'

class ContaFisica(Conta):
    def __init__(self, nome: str, telefone_contato: str, cpf:str) -> None:
        super().__init__(nome, telefone_contato)
        self.cpf = cpf

    def __repr__(self) -> str:
        return f'Nome: {self.nome}, Telefone: {self.telefone_contato}, CPF: {self.cpf}'


