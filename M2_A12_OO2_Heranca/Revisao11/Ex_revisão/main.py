from cls_pessoa import Pessoa

def cadastrar() -> Pessoa:
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    cpf = input("Digite o cpf: ")

    nw_pessoa = Pessoa(nome,idade,cpf)
    return nw_pessoa

def fazer_acao(pess: Pessoa) -> None:
    flg_agir = True

    while flg_agir:
        print('-'*30)
        print('1 Para andar\n2 para correr\n3 para parar\n4Sair ações')
        op = int(input("Digite a opcao: "))

        match op:
            case 1:
                pess.andar()
            case 2:
                pess.correr()
            case 3:
                pess.parar()
            case 4:
                break
            case _:
                print("Digite apenas umas das opções")
        

def main():
    
    pessoa1 = Pessoa("Guilherme",40,"001.001.001-01")
    pessoa2 = Pessoa("Bi",40,"002.002.001-02")

    pessoa1.correr()
    pessoa2.andar()

    print(pessoa1)
    print(pessoa2)

def main2():
    flg_app = True
    

    while flg_app:
        print("1: cadastrar\n 2:Mudar status\n3:Mostrar pessoa\n4:Sair")
        op = int(input("Digite a opção:"))
        match op:
            case 1:
                pess = cadastrar()
            case 2:
                fazer_acao(pess)
            case 3:
                print(pess)    
            case 4:
                print("Programa abortado")
                break
            case _:
                print("Digite apenas as opcoes desejadas")

if __name__ == '__main__':
    main2()