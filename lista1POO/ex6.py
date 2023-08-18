# Classe TV: Faça um programa que simule um televisor criando-o como um objeto.
# O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume.
# Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.


class TV:
    def __init__(self):
        self.vol = 100
        self.canal = 0

    def mudarCanal(self,canal):
        if(canal<0):
            print("Canal negativo n existe")
        if(canal > 500):
            print("Canal invalido")
        else:
            self.canal = canal
    def aumentarVolume(self,volume):
        if(volume<0):
            print("Valor invalido")
        if(volume > 100):
            print("Maior que o volume max")
        if((volume + self.vol) > 100):
            print("Maior que o volume max")
        else:
            self.vol += volume


    def diminuirVolume(self,volume):
        if (volume < 0):
            print("Valor invalido")
        if(volume > self.vol):
            self.vol = 0
            print("TV no mudo")
        else:
            self.vol -= volume

    def retornarValores(self):
        return f"Volume atual: {self.vol}, Canal Atual: {self.canal}"

tv = TV()

tv.aumentarVolume(10)
print(tv.retornarValores())
tv.diminuirVolume(50)
print(tv.retornarValores())
tv.diminuirVolume(10000)
print(tv.retornarValores())
tv.mudarCanal(300)
print(tv.retornarValores())
tv.mudarCanal(600)
print(print(tv.retornarValores()))


