class Funcionario:
    def __init__(self,id:int, nome:str,cargo:str,salario:float) -> None:
        self.id = id
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
    def __repr__(self):
        return f"id:{self.id}, Nome: {self.nome}, Cargo: {self.cargo}, Salario: {self.salario}"

class Empresa:
    
    def __init__(self) -> None:
        self.funcionarios = []

    def adicionar_funcionarios(self, nome:str,cargo:str,salario:float) -> None:
        nw_id = len(self.funcionarios) + 1
         
        nw_func = Funcionario(nw_id,nome,cargo,salario)
        self.funcionarios.append(nw_func)
 
    def listar_funcionarios(self)->None:
        for func in self.funcionarios:
            print(f"{func}")

    def __localizar_list_pos_por_id(self, id: int) -> int:
        for i, funcionario in enumerate(self.funcionarios):
            if funcionario.id == id:
                return i
        return -1

    def apagar_funcionario(self,id:int)->None:
        lst_pos = self.__localizar_list_pos_por_id(id)
        if lst_pos == -1:
            print("erro: Funcionario não existe")
        else:
            self.funcionarios.pop(lst_pos)
            print("Funcionario removido")


empresa1 = Empresa()
empresa1.adicionar_funcionarios("Gui","Analista",100)
empresa1.adicionar_funcionarios("Pedro","Analista",200)
empresa1.adicionar_funcionarios("Joao","Analista",300)

empresa1.listar_funcionarios()

print("-"*30)
print("Apagar id 2")
empresa1.apagar_funcionario(2)
empresa1.listar_funcionarios()

print("-"*30)
print("Apagar id 3")
empresa1.apagar_funcionario(3)
empresa1.listar_funcionarios()



