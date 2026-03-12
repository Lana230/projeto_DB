from models.pessoa import Pessoa

class Enfermeiro(Pessoa):
    def __init__(self, cpf, nome, id_ubs, cip):
        super().__init__(cpf, nome, id_ubs)
        self.cip = cip
    
    def exibir(self):
        super().exibir()
        print(f"CIP: {self.cip}")