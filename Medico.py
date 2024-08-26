
class Medico:
    def __init__(self, nome, especialidade, crmv):
        self.nome = nome
        self.especialidade = especialidade
        self.__crmv = crmv

    def get_crm(self):
        return self.__crmv

    def __str__(self):
        return f"Veterinário: {self.nome}, Especialidade: {self.especialidade}, CRM: {self.__crmv}"
