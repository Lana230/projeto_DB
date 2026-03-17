from models.medico import Medico
from models.vaccine import Vaccine
from models.ubs import Ubs
from enum import Enum

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.agendamento import Agendamento

class Tipo_atendimento(Enum):
    CONSULTA = "Consulta"
    VACINA = "Vacina"

class Fila_atendimento:
    
    def __init__(self, ubs: Ubs, tipo_atendimento, data_fila, quantidade_maxima, medico: Medico, vacina: Vaccine):
        
        self.ubs = ubs
        self.tipo_atendimento = tipo_atendimento
        self.data_fila = data_fila
        self.quantidade_maxima = quantidade_maxima
        self.medico = medico
        self.vacina = vacina
        self.agendamentos = []
    
    def adicionar_agendamento(self, agendamento: "Agendamento"):
        self.agendamentos.append(agendamento)
    