class Bichinho:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def __str__(self):
        return f"Atributos do bichinho: Nome: {self.nome} Fome: {self.fome} Saúde: {self.saude} Idade: {self.idade}"

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

    def setFome(self, comida):
        self.fome += comida/2

    def setSaude(self, novaSaude):
        self.saude = novaSaude

    def setIdade(self, novaIdade):
        self.idade = novaIdade

    def getHumor(self, tempoDeBrincar=0):
        humor = self.saude / 2 + self.fome / 2
        humor += tempoDeBrincar/5
        return humor


bichinhos = [Bichinho("Pikachu", 7, 3, 10), Bichinho("Chimchar", 3, 4, 10), Bichinho("Jigglypuff", 2, 6, 10),
             Bichinho("Gengar", 2, 4, 5)]
for bichinho in bichinhos:
    bichinho.setFome(2)
    print(bichinho)