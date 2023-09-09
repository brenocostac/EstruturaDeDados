# Classe Conta Corrente: Crie uma classe para implementar uma conta corrente.
# A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo.
# Os métodos são os seguintes: alterarNome, depósito e saque;
# No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.

class ContaCorrente:
    def __init__(self, numeroDaConta,nomeDoCorrentista,saldo = 0):
        self.numeroDaConta = numeroDaConta
        self.nomeDoCorrentista = nomeDoCorrentista
        self.saldo = saldo

    def setNome(self,nome):
        self.nomeDoCorrentista = nome

    def deposito(self, valorDeposito):
        self.saldo += valorDeposito

    def saque(self, valorSaque):
        self.saldo -= valorSaque

    def getConta(self):
        return f"Saldo atual: {self.saldo}, Nome:{self.nomeDoCorrentista}"


conta = ContaCorrente(123,"Junior")

print(conta.retornarValor())

conta.deposito(10000)
conta.saque(500)
print(conta.getConta())

