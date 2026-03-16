from models.pessoa import *

class Enfermeiro(Pessoa):
    def __init__(self, cpf, nome, ubs: Ubs, cip):
        super().__init__(cpf, nome, ubs)
        self.cip = cip
    
    def exibir(self):
        super().exibir()
        print(f"CIP: {self.cip}")