from classes import Conta, ContaFisica,ContaJuridica

def mostrar_dados_conta(Conta:Conta):
    print(Conta)

c_fisica1 = ContaFisica("Joao","(31)9999-9999","000.000.000-01")
c_juridica1 = ContaJuridica("Joao","(31)9999-9999","000.000.000/0001-00")

print("Mostrando dados conta fisica")
print(c_fisica1)
#Receber um dicionario da conta
print(c_fisica1.__dict__)


print("Mostrando dados conta Juridica")
print(c_juridica1)


