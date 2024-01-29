class Calculadora:

    def somar(self, *args):
        return sum(args)
    
    def subtrair(self,*args):
        [total, *numeros] = args
        for num in numeros:
            total = total - num
        # result = args[0]
        # i = 0
        # for num in args:
        #     if not i == 0:
        #         result = result - num
        #     i += 1
        # return result
        return total
    
    def multiplicar(self, *args):
        result = 1
        for num in args:
            result = result * num
        return result
    
    def dividir(self,num,div):
        if div == 0:
            return "Erro divisão por 0"
        else:
            return num/div
        

calc1 = Calculadora()

print(f"Resultado Soma: {calc1.somar(10,10,10,10)}")

print(f"Resultado subtração: {calc1.subtrair(100,10,10)}")

print(f"Resultado multiplicacao: {calc1.multiplicar(4,2,2,2)}")

print(f"Resultado divisão: {calc1.dividir(100,2)}")