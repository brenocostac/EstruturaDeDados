class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def getNome(self):
        return self.nome

    def getSalario(self):
        return self.salario

    def aumentarSalario(self, percentual):
        self.salario += self.salario * (percentual/100)


harry = Funcionario('Harry', 25000)
harry.aumentarSalario(10)
print(f"O novo salário do funcionário {harry.getNome()} é R${harry.getSalario():.2f}")