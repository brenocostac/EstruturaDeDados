# Classe Quadrado: Crie uma classe que modele um quadrado:

# Atributos: Tamanho do lado
# Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;


class Quadrado:
    def __init__(self,lado):
        self.lado = lado

    def mudarValorDoLado(self,lado):
        self.lado = lado

    def getLado(self):
        return self.lado

    def calcularArea(self):
        return self.getLado() ** 2


quadrado = Quadrado(2)


print(quadrado.calcularArea())

print(quadrado.getLado())

quadrado.mudarValorDoLado(10)

print(quadrado.getLado())