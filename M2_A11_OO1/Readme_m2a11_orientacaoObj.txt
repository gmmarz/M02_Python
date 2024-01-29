Curso python modulo 2 python
orientação de objetos
init_classe - primeiro arquivo com exemplo de classe

Para a criação de uma classe
por convenção a primeira letra da classe deve ser maiúscula.

classe: é o molde para abstração de algo do mundo real
        composta de atributos que são as caracteristicas
        metodos que são as ações.

objeto: é a representação real da classe.

Existe o metodo __repr__ que possibilita criar uma representação do objeto. 

exemplo: 

dont pad - codigo
inf219-0801

class Cachorro:
    def __init__(self,nome, raca, idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade

    def __repr__(self) -> str:
        return f"Nome: {self.nome}, Raca: {self.raca}, Idade: {self.idade} "