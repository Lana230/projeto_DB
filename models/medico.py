from models.pessoa import Pessoa

class Medico(Pessoa):
    def __init__(self, cpf, nome, id_ubs, crm, especialidade):
        super().__init__(cpf, nome, id_ubs)
        self.crm = crm
        self.especialidade = especialidade
    
    def exibir(self):
            super().exibir()
            print(f"CRM: {self.crm}")
            print(f"Especialidade: {self.especialidade}")