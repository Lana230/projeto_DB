from models.pessoa import Pessoa, Ubs

class Enfermeiro(Pessoa):
    def __init__(self, nome_pessoa, estado_civil, ubs: Ubs, cip):
        super().__init__(nome_pessoa, estado_civil, ubs)
        
        self.cip = cip
    
    def exibir(self):
        super().exibir()
        
        print(f"CIP: {self.cip}")