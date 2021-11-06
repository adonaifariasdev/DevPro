# Classe Pessoa: Crie uma classe que modele uma pessoa:
#     Atributos: nome, idade, peso e altura
#     Métodos: Envelhercer, engordar, emagrecer, crescer.
#     Obs: Por padrão, a cada ano que nossa pessoa envelhece,
#     sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        if self.idade < 21:
            self.altura += 0.5
        self.idade += 1

    def engordar(self):
        self.peso += 1

    def emagrecer(self):
        self.peso -= 0.5

    def crescer(self):
        self.altura -= 0.5

otavio = Pessoa('Otavio', 2, 12, 80)
adonai = Pessoa('Adonai', 39, 87, 1.65)
for _ in range(22):
    otavio.envelhecer()
    otavio.engordar()
    print(f'Idade de {otavio.nome} é: {otavio.idade}. E sua altura é {otavio.altura}cm')
    print(f'Peso é {otavio.peso}Kg')
    print()
    print()
    adonai.emagrecer()
    adonai.crescer()
    print(f'Peso é {adonai.peso}Kg')
    print(f'Altura é {adonai.altura}cm')