from models.pessoa import Pessoa

class Dependente:
    
    def __init__(self, responsavel: Pessoa, dependente: Pessoa, parentesco):
        
        self.responsavel = responsavel
        self.dependente = dependente
        self.parentesco = parentesco
    
    def exibir(self):
        print("--- Dependente ---")
        print(f"Nome do responsável: {self.responsavel.nome_pessoa}")
        print(f"Nome do dependente: {self.dependente}")
        print(f"Parentesco: {self.parentesco}")
        print("-------------------\n")