from classes import Pessoa, Funcionario

def main() -> None:
    flg_app = True

    p1 = Pessoa("Gui",40, "xxx.xxx.xxx-xx")
    print(f' O CPF do {p1.nome} é {p1.cpf}')

    print(f'Alterando a idade de {p1.nome} de modo errado')
    p1.idade = 1
    print(f'A idade continua {p1.idade}')

    print(f'Alterando a idade de {p1.nome} de modo correto')
    p1.idade = 45
    print(f'A idade foi alterada para {p1.idade}')

def test():

    func1 = Funcionario('Jao', 41,"xxx.xxxx.xxxx","Programador")

    print(func1)
 


if __name__ == "__main__":
    test()