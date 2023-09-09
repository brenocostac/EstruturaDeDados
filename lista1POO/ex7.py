# Classe Bichinho Virtual: Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):

# Atributos: Nome, Fome, Saúde e Idade
# Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade
# Obs: Existe mais uma informação que devemos levar em consideração,
# o Humor do nosso tamagushi, este humor é uma combinação entre os atributos Fome e Saúde,
# ou seja, um campo calculado, então não devemos criar um atributo para armazenar esta informação
# por que ela pode ser calculada a qualquer momento.

class Bichinho:
    def __init__(self,nome,fome,saude,idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterarNome(self,nome):
        self.nome = nome

    def alterarFome(self,fome):
        self.fome = fome

    def alterarSaude(self,saude):
        self.saude = saude

    def alterarIdade(self,idade):
        self.idade

    def nome(self):
        return self.nome

    def fome(self):
        return self.fome

    def saude(self):
        return self.saude

    def idade(self):
        return self.idade

    def retornarHumor(self):
        return (self.fome + self.saude)/2


bichinho = Bichinho("Gengar", 80, 70, 6)
print(bichinho.retornarHumor())