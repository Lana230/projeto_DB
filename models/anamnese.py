from models.cidadao import Cidadao
from models.appointment import Appointment

class Anamnese:
    def __init__(self, cidadao: Cidadao, appointment: Appointment, peso, altura, pressao_arterial):
        self.cidadao = cidadao
        self.appointment = appointment
        self.peso = peso
        self.altura = altura
        self.pressao_arterial = pressao_arterial
        
    def exibir(self):
        print("--- Anamnese ---")
        print(f"Nome do paciente: {self.cidadao.nome}")
        print(f"Peso: {self.peso}")
        print(f"Altura: {self.altura}")
        print(f"Pressão arterial: {self.pressao_arterial}")
        print("-----------------\n")