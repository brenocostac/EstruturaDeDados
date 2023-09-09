# Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho
# (estomago) e pelo menos os métodos comer(), verBucho() e digerir().
# Faça um programa ou teste interativamente, criando pelo menos dois macacos,
# alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do
# estomago a cada refeição. Experimente fazer com que um macaco coma o outro.
# É possível criar um macaco canibal?


class Macaco:
    def __init__(self,nome,bucho=[]):
        self.nome = nome
        self.bucho = bucho

    def comer(self,comida):
        self.bucho.append(comida)

    def digerir(self,comida):
        for comidas in self.bucho:
            if comidas == comida:
                self.bucho.remove(comida)

    def verBucho(self):
        print("Comidas no bucho: ")
        for comida in self.bucho:
            print(comida,end=' ')
        print()

macaco = Macaco("Jorge")
macaco.comer("maça")
macaco.comer("melao")
macaco.comer("macaco")
macaco.verBucho()
macaco.digerir("melao")
macaco.verBucho()
macaco2 = Macaco('Xiita')
print(macaco2.ver_bucho())
macaco2.comer(macaco)
print(macaco2.ver_bucho())
macaco2.digerir(macaco)
print(macaco2.ver_bucho())
macaco2.comer("Melancia")
print(macaco2.ver_bucho())
