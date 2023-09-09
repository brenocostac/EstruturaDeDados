class Bichinho:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def getNome(self):
        return self.nome

    def getFome(self):
        return self.fome

    def getSaude(self):
        return self.saude

    def getIdade(self):
        return self.idade

    def setNome(self, novoNome):
        self.nome = novoNome

    def serFome(self, comida):
        self.fome += comida/2

    def setSaude(self, novaSaude):
        self.saude = novaSaude

    def setIdade(self, novaIdade):
        self.idade = novaIdade

    def getHumor(self, tempoDeBrincar=0):
        humor = self.saude / 2 + self.fome / 2
        humor += tempoDeBrincar/5
        return humor