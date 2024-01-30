"""
    Associação: 1 Aluno - 1 Turma
                1Turma - N alunos
                1 Professor - N Turmas
                1Turma - 1 Professor
"""


class Pessoa:
    def __init__(self,nome:str,cpf:str) -> None:
        self.nome = nome
        self.__cpf = cpf
    
    @property
    def cpf(self) -> str:
        return self.__cpf
    
    def __repr__(self) -> str:
        pass

class Aluno(Pessoa):
    def __init__(self, nome: str, cpf: str,endereco:str, nota:float, turma) -> None:
        super().__init__(nome, cpf)
        self.endereco = endereco
        self.nota = nota
        self.turma = turma
        turma.adicionar_aluno(self)
    
    def __repr__(self) -> str:
        return {f'Aluno: Nome:{self.nome}, CPF: {self.cpf}'}


class Turma:
    def __init__(self, numero_turma:str,curso:str, professor) -> None:
        self._numero_turma = numero_turma
        self.curso = curso
        self.professor = professor
        self.alunos = []

        professor.adicionar_turma(self)

    @property
    def numero_turma(self) -> int:
        return self._numero_turma
    
    @numero_turma.setter
    def numero_turma(self,novo_numero) -> None:
        self._numero_turma = novo_numero
    
    def adicionar_aluno(self, nw_aluno:Aluno) -> None:
        self.alunos.append(nw_aluno)
    
    def listar_nomes_alunos(self) -> list[str]:
        lst_nomes = [aluno.nome for aluno in self.alunos]
        return lst_nomes
    
    def __repr__(self) -> str:
        nome_alunos = self.listar_nomes_alunos()
        return f'Turma Numero:{self.numero_turma}, Professor turma: {self.professor}, Alunos Turma:{nome_alunos}'


class Professor(Pessoa):
    def __init__(self, nome: str, cpf: str, especialidade:str) -> None:
        super().__init__(nome, cpf)
        self.especialidade = especialidade
        self.turmas = []

    def __repr__(self) -> str:
        return f'Professor: Nome {self.nome}, CPF: {self.cpf}, Especialidade: {self.especialidade}'
    
    def adicionar_turma(self, nw_turma:Turma):
        self.turmas.append(nw_turma)

class Turma:
    def __init__(self, numero_turma:str,curso:str, professor:Professor) -> None:
        self._numero_turma = numero_turma
        self.curso = curso
        self.professor = professor
        self.alunos = []

    @property
    def numero_turma(self) -> int:
        return self._numero_turma
    
    @numero_turma.setter
    def numero_turma(self,novo_numero) -> None:
        self._numero_turma = novo_numero
    
    def adicionar_alunos(self, nw_alunos_lst:list) -> None:
        for nw_aluno in nw_alunos_lst:
            self.alunos.append(nw_aluno)
    
    def listar_nomes_alunos(self) -> list[str]:
        lst_nomes = [aluno.nome for aluno in self.alunos]
        return lst_nomes
    
    def __repr__(self) -> str:
        nome_alunos = self.listar_nomes_alunos()
        return f'Turma Numero:{self.numero_turma}, Professor turma: {self.professor}, Alunos Turma:{nome_alunos}'

if __name__ == '__main__':
    print('Este é um modulo, não deve ser executado diretamente')