from models import *

from database.conexao import connection

class AgendamentoRepository:
    
    def salvar(self, agendamento: Agendamento, fila: Fila_atendimento):
        con = connection()
        con = con.cursor()
        
        cursor.execute("INSERT INTO agendamento (num_sus, data_solicitacao, status, hora_agendamento, posicao_atual, prioridade_calculada, motivo_prioridade, id_fila) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (agendamento.cidadao.num_sus, agendamento.data_solicitacao, agendamento.status, agendamento.hora_agendamento, agendamento.posicao_atual, agendamento.prioridade_calculada, agendamento.motivo_prioridade, fila.id_fila))
        
        agendamento.id_agendamento = cursor.lastrowid
        
        cursor.commit()
        con.close()
        
        return agendamento