from classes import Conta

def main():

    c1 = Conta("Gui","(11)111.111.11","xxx.xxx.xxx-xx")
    
    print(f'Mostrando saldo inicial: {c1.saldo}')

    print('-'*30)
    print('Realizando um deposito de 100 reais')
    c1.deposito(100)
    print(f'Mostrando o novo saldo {c1.saldo}')
 
if __name__ == "__main__":
    main()
