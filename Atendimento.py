
from datetime import date

class Atendimento:
    def __init__(self, animal, medico, data, descricao):
        self.animal = animal
        self.medico = medico
        self.__data = data
        self.descricao = descricao

    def get_data(self):
        return self.__data

    def __str__(self):
        return f"Atendimento em {self.__data}: {self.animal.get_nome()} foi atendido por {self.medico.nome}. Descrição: {self.descricao}"
