
class Animal:
    def __init__(self, nome, especie, idade, dono):
        self.__nome = nome
        self.especie = especie
        self.idade = idade
        self.__dono = dono

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_dono(self):
        return self.__dono

    def set_dono(self, dono):
        self.__dono = dono

    def __str__(self):
        return f"Animal: {self.__nome}, Espécie: {self.especie}, Idade: {self.idade} anos, Dono: {self.__dono}"
