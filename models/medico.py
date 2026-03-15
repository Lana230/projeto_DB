from models.pessoa import *

class Medico(Pessoa):
    def __init__(self, cpf, nome, ubs: Ubs, crm, especialidade):
        super().__init__(cpf, nome, ubs)
        self.crm = crm
        self.especialidade = especialidade
    
    def exibir(self):
            super().exibir()
            print(f"CRM: {self.crm}")
            print(f"Especialidade: {self.especialidade}")