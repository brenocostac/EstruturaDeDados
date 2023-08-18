 # Classe Bola: Crie uma classe que modele uma bola:

# Atributos: Cor, circunferência, material
# Métodos: trocaCor e mostraCor


class Bola:
    def __init__(self,Cor,circunferencia,material):
        self.Cor = Cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self,Cor):
        self.Cor = Cor

    def mostraCor(self):
        return self.Cor



bola = Bola("preto",12,"plastico")
print(bola.mostraCor())
bola.trocaCor("Azul")
print(bola.mostraCor())