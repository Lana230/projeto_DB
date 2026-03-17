from models.cidadao import Cidadao

class Anamnese:
    def __init__(self, cidadao: Cidadao, data_anamnese, peso, altura, pressao_arterial):
        
        self.id_anamnese = None
        self.cidadao = cidadao
        self.data_anamnese = data_anamnese
        self.peso = peso
        self.altura = altura
        self.pressao_arterial = pressao_arterial
        
    def exibir(self):
        print("--- Anamnese ---")
        print(f"Nome do paciente: {self.cidadao.nome}")
        print(f"Data: {self.data_anamnese}")
        print(f"Peso: {self.peso}")
        print(f"Altura: {self.altura}")
        print(f"Pressão arterial: {self.pressao_arterial}")
        print("-----------------\n")