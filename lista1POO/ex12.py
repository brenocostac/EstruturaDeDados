class Conta:
    def __init__(self, numero, nome, saldo=0):
        self.numero = numero
        self.nome = nome
        self.saldo = saldo

    def alterarNome(self, novo_nome):
        self.nome = novo_nome

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        self.saldo -= valor


class ContaInvestimento(Conta):
    def __init__(self, numero, nome, saldo=0.0, taxaJuros=0.0):
        super().__init__(numero, nome, saldo)
        self.taxaJuros = taxaJuros

    def adicioneJuros(self):
        self.saldo += self.saldo * (self.taxaJuros / 100)


conta2 = ContaInvestimento(12345, 'Breno', 1000, 10)
conta2.adicioneJuros()
conta2.adicioneJuros()
conta2.adicioneJuros()
conta2.adicioneJuros()
conta2.adicioneJuros()
print(f"O novo saldo da conta é {conta2.saldo}")