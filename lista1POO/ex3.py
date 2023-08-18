# Classe Retangulo: Crie uma classe que modele um retangulo:

# Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
# Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;


class Retangulo:
    def __init__(self,comprimento,largura):
        self.comprimento = comprimento
        self.largura = largura

    def mudarValorDoComprimento(self,comprimento):
        self.comprimento = comprimento

    def mudarValorDaLargura(self,largura):
        self.largura = largura

    def retornarLados(self):
        return f"{self.largura}  {self.comprimento}"

    def calcularArea(self):
        return self.largura * self.comprimento

    def perimetro(self):
        return 2 * self.largura + 2 * self.comprimento


retangulo = Retangulo(5,10)

print(retangulo.retornarLados())
print(retangulo.perimetro())
print(retangulo.calcularArea())