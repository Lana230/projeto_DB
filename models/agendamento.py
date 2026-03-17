from models.cidadao import Cidadao

from enum import Enum

class StatusAgendamento(Enum):
    PENDENTE = "Pendente"
    CONFIRMADO = "Confirmado"
    EM_ESPERA = "Em espera"
    CHAMADO = "Chamado"
    EM_ATENDIMENTO = "Em atendimento"
    CONCLUIDO = "Concluido"
    CANCELADO = "Cancelado"
    NAO_COMPARECEU = "Não compareceu"
    REMARCADO = "Remarcado"
    PRIORIDADE = "Prioridade"

class Agendamento:
    
    def __init__(self, cidadao: Cidadao, data_solicitacao, hora_agendamento, posicao_atual, prioridade_calculada = 0, motivo_prioridade = None, status = StatusAgendamento.PENDENTE):
        
        self.cidadao = cidadao
        self.data_solicitacao = data_solicitacao
        self.hora_agendamento = hora_agendamento
        self.posicao_atual = posicao_atual
        self.prioridade_calculada = prioridade_calculada
        self.motivo_prioridade = motivo_prioridade
        self.status = status
    
    def exibir(self):
        print("---- Agendamento ---")
        print(f"SUS {self.cidadao.sus}")
        print(f"Nome do paciente: {self.cidadao.nome_pessoa}")
        print(f"Data da solicitação: {self.data_solicitacao}")
        print(f"Hora do agendamento: {self.hora_agendamento}")
        print(f"Posição atual: {self.posicao_atual}")
        print(f"Motivo da prioridade: {self.motivo_prioridade}")
        print(f"Status: {self.status}")
        
        