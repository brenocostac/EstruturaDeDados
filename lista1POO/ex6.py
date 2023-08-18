# Classe TV: Faça um programa que simule um televisor criando-o como um objeto.
# O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume.
# Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.


class TV:
    def __init__(self):
        self.vol = 100
        self.canal = 0

    def mudarCanal(self,canal):
        if(canal > 0 and canal <= 500):
            self.canal = canal
        else:
            print("Canal invalido")


    def ajusteDeVolume(self,volume):
        if  0 <= volume + self.vol <= 100 :
            self.vol += volume
        else:
            print("Ajuste de volume invalido")

    def retornarValores(self):
        return f"Volume atual: {self.vol}, Canal Atual: {self.canal}"

tv = TV()

tv.ajusteDeVolume(10)
print(tv.retornarValores())
tv.ajusteDeVolume(-50)
print(tv.retornarValores())
tv.ajusteDeVolume(-10)
print(tv.retornarValores())
tv.mudarCanal(300)
print(tv.retornarValores())
tv.mudarCanal(600)
print(print(tv.retornarValores()))


