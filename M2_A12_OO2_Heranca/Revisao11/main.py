from Cls_carro import Carro

def main():
    # carro1 = Carro() #Exemplo de quando os atributos estavam fixos
    carro1 = Carro("Azul", 4, "BMW")
    carro1.acelerar()
    print(carro1)

if __name__ == '__main__':
    main()
