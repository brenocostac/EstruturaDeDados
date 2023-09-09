# Classe Pessoa
'''
atts :  nome, idade, peso, altura
metodos : envelhecer , engordar , emagrecer ,crescer
'''

class Pessoa:
    def __init__(self,nome,idade,peso,altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura


    def retornarValores(self):
        return f"Idade: {self.idade}, Nome: {self.nome}, peso: {self.peso}, altura: {self.altura}"

    def envelhecer(self, novaIdade):
        if novaIdade > self.idade:
            if self.idade < 21:
                for i in range(self.idade, novaIdade):
                    if i == 21:
                        break
                    self.altura += 0.05
                self.crescer(self.altura)
            self.idade = novaIdade

    def engordar(self, peso):
         self.peso += peso

    def emmagrecer(self, peso):
        self.peso -= peso

    def crescer(self, altura):
        self.altura += altura


pessoa = Pessoa("Fodase Jr", 17, 75, 1.89)

print(pessoa.retornarValores())

pessoa.engordar(10)
pessoa.emmagrecer(5)
pessoa.crescer(0.10)
pessoa.envelhecer(21)
print(pessoa.retornarValores())

