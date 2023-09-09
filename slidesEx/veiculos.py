"""
Esta e uma classe generica de veiculo
"""


class Veiculo:
    def __init__(self, tipo):
        self.tipo = tipo

    """
    Esta e uma classe para o veiculo se mover
    """

    def andar(self):
        print("Andando")


"""
Esta e uma classe generica de veiculo de +4 rodas
"""


class VMaisDe4Rodas(Veiculo):
    def __init__(self, tipo, nRodas):
        super().__init__(tipo)
        self.nRodas = nRodas


"""
Esta e uma classe generica de veiculo de 4 rodas
"""


class VQuatroRodas(Veiculo):
    def __init__(self, tipo):
        super().__init__(tipo)
        self.nRodas = 4


"""
Esta e uma classe generica de veiculo de 2 rodas
"""


class VDuasRodas(Veiculo):
    def __init__(self, tipo):
        super().__init__(tipo)
        self.nRodas = 2


"""
Esta e uma classe generica de veiculo motorizado
"""


class VMotorizado(Veiculo):
    def __init__(self, tipo):
        super().__init__(tipo)
        self.motor = True

    """
    Este e um metodo que permite veiculos motorizados acelerar 
    """

    def acelerar(self):
        print("Acelerando...")


"""
Esta e uma classe generica de veiculo nao motorizado
"""


class VSemMotor(Veiculo):
    def __init__(self, tipo):
        super().__init__(tipo)
        self.motor = False


class Bicicleta(VDuasRodas):
    def __init__(self, tipo):
        super().__init__(tipo)

    def andar(self):
        print("pedalando")


class Caminhao(VMaisDe4Rodas, VMotorizado):
    def __init__(self, tipo, nRodas, carga):
        super().__init__(tipo, nRodas)
        self.carga = carga


    def __str__(self):
        return f"Tipo: {self.tipo}, Rodas: {self.nRodas}, Carga: {self.carga}"
    """
    Metodo para liberar a carga de um caminhao
    """

    def liberarCarga(self):
        self.carga = 0


class Moto(VMotorizado, VDuasRodas):
    def __init__(self, tipo):
        super().__init__(tipo)


class Carro(VMotorizado, VQuatroRodas):
    def __init__(self, tipo):
        super().__init__(tipo)


class Camionete(Caminhao):
    def __init__(self, tipo, nRodas, carga):
        super().__init__(tipo, nRodas, carga)
        
    def __str__(self):
        camionete_info = super().__str__()
        return f"Camionete: {camionete_info}"


minha_camionete = Camionete("Camionete Tipo A", 4, 1000)

print(minha_camionete)