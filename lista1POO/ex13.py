class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def getNome(self):
        return self.nome

    def getSalario(self):
        return self.salario


funcionario1 = Funcionario('Junior', 3000)
print(f"O nome do funcionário 1 é {funcionario1.getNome()}")
print(f"O salário do funcionário 1 é R${funcionario1.getSalario():.2f}")