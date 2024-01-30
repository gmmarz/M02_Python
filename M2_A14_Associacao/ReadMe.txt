Aula de revisão OO classe e encapisulamento

dontpad - inf219-2901


Exemplo associação:
"""
    CRIE UM SISTEMA DE ESCOLA
	PESSOA 
		- nome
		- cpf(privado)
	ALUNO (PESSOA)
		- endereco
		- nota
	PROFESSOR (PESSOA)
		- especialidade
	TURMA
		- numero_turma (protegida)
		- curso
"""

class Pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.__cpf = cpf

    @property
    def cpf(self):
        return self.__cpf

class Aluno(Pessoa):
    def __init__(self, nome, cpf, endereco, nota, turma):
        super().__init__(nome, cpf)

        self.endereco = endereco
        self.nota = nota
        self.turma = turma

        turma.adicionar_aluno(self)


class Turma:
    def __init__(self, numero_turma, curso, professor):
        self._numero_turma = numero_turma
        self.curso = curso
        self.professor = professor
        self.alunos = []

        professor.adicionar_turma(self)

    @property
    def numero_turma(self):
        return self._numero_turma
    
    def adicionar_aluno(self, aluno: Aluno):
        self.alunos.append(aluno)
    
class Professor(Pessoa):
    def __init__(self, nome, cpf, especialidade):
        super().__init__(nome, cpf)

        self.especialidade = especialidade
        self.turmas = []

    def adicionar_turma(self, turma: Turma):
        self.turmas.append(turma)
    
professor1 = Professor("Not", "00000000034", "DEV FS")
turma1 = Turma("219", "DEV FS", professor1)
aluno1 = Aluno("Wilson", "00000000012", "Paraíso", 11, turma1)

print(professor1.turmas[0])