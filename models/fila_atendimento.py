from models.medico import Medico
from models.vaccine import Vaccine
from models.ubs import Ubs
from enum import Enum

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.agendamento import Agendamento

class TipoAtendimento(Enum):
    CONSULTA = "Consulta"
    VACINA = "Vacina"

class Fila_atendimento:
    
    def __init__(self, ubs: Ubs, tipo_atendimento, data_fila, quantidade_maxima, medico: Medico=None, vacina: Vaccine=None):
        
        self.id_fila = None
        self.ubs = ubs
        self.tipo_atendimento = tipo_atendimento
        self.data_fila = data_fila
        self.quantidade_maxima = quantidade_maxima
        self.medico = medico
        self.vacina = vacina
        self.agendamentos = []
    
    def adicionar_agendamento(self, agendamento: "Agendamento"):
        self.agendamentos.append(agendamento)
    
    @classmethod
    def criar_fila(classe, ubs: Ubs, tipo_atendimento, data_fila, quantidade_maxima, medico: Medico=None, vacina: Vaccine=None):
        if not isinstance(tipo_atendimento, TipoAtendimento):
            try:
                tipo_atendimento = TipoAtendimento(tipo_atendimento)
            except ValueError:
                raise ValueError("Tipo de atendimento inválido")
            
        if tipo_atendimento == TipoAtendimento.CONSULTA:
             if medico is None or vacina is not None:
                 raise ValueError("Fila de consulta deve ter apenas médico")
        elif tipo_atendimento == TipoAtendimento.VACINA:
            if vacina is None or medico is not None:
                raise ValueError("Fila de vacinação deve ter apenas vacina")
        
        if quantidade_maxima <= 0:
            raise ValueError("Quantidade máxima deve ser maior que zero")
        
        if ubs is None:
            raise ValueError("UBS é obrigatória")
        
        return classe(ubs, tipo_atendimento, data_fila, quantidade_maxima, medico, vacina)