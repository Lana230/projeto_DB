from models.cidadao import Cidadao
from models.appointment import Appointment

class Anamnese:
    def __init__(self, cidadao: Cidadao, appointment: Appointment, peso, altura, pressao_arterial):
        self.cidadao = cidadao
        self.appointment = appointment
        self.peso = peso
        self.altura = altura
        self.pressao_arterial = pressao_arterial
        
    def adicionar_id(self, id_anamnese):
        self.id_anamnese = id_anamnese