from enum import Enum

class Tipo_atendimento(Enum):
    CONSULTA = "Consulta"
    VACINA = "Vacina"
    
class StatusFila(Enum):
    AGUARDANDO = 0
    CHAMADO = 1
    EM_ATENDIMENTO = 2
    ATENDIDO = 3
    NAO_COMPARECEU = 4
    CANCELADO = 5
    REMARCADO = 6
    PRIORIDADE = 7
    
    #Aguardando - pessoa esta esperando na fila
    #Chamado - a pessoa foi chamada
    #Em atendimento - a pessoa esta sendo atendida no momento
    #Atendido - atendimento finalizado
    #Nao compareceu - pessoa foi chamada mas nao apareceu
    #Cancelado - atendimento foi cancelado
    #Remarcado - atendimento foi reagendado
    #Prioridade - pessoa recebeu prioridade na fila

class Fila_atendimento:
    
    def __init__(self, sus, id_ubs, tipo_atendimento, data_solicitacao, posicao_atual, status, prioridade_calculada, motivo_prioridade):
        self.sus = sus
        self.id_ubs = id_ubs
        self.tipo_atendimento = tipo_atendimento
        self.data_solicitacao = data_solicitacao
        self.posicao_atual = posicao_atual
        self.status = status
        self.prioridade_calculada = prioridade_calculada
        self.motivo_prioridade = motivo_prioridade
    
    def adicionar_id(self, id_fila):
        self.id_fila = id_fila