import sqlite3
from models import Cidadao, StatusAgendamento, Fila_atendimento, Agendamento
from database.conexao import connection
from .cidadao_repository import CidadaoRepository

class AgendamentoRepository:
    
    def __init__(self):
        self.cidadao_repo = CidadaoRepository()
    
    def salvar(self, agendamento: Agendamento):
        con = connection()
        cursor = con.cursor()
        
        cursor.execute("""
            INSERT INTO agendamento (
                num_sus, data_solicitacao, status, 
                hora_agendamento, posicao_atual, prioridade_calculada, 
                motivo_prioridade, id_fila
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    agendamento.cidadao.num_sus, 
                    agendamento.data_solicitacao, 
                    agendamento.status.value, 
                    agendamento.hora_agendamento, 
                    agendamento.posicao_atual, 
                    agendamento.prioridade_calculada, 
                    agendamento.motivo_prioridade, 
                    agendamento.id_fila
            ))
        
        agendamento.id_agendamento = cursor.lastrowid
        
        con.commit()
        con.close()
        
        return agendamento
    
    def construir_objeto(self, rows):
        agendamentos = []
        
        for row in rows:
            if row is None:
                continue
            
            cidadao = self.cidadao_repo.buscar_por_sus(row["num_sus"])
            
            ag = Agendamento(
                cidadao=cidadao,
                data_solicitacao=row["data_solicitacao"],
                hora_agendamento=row["hora_agendamento"],
                posicao_atual=row["posicao_atual"],
                status=StatusAgendamento(row["status"]),
                prioridade_calculada=row["prioridade_calculada"],
                motivo_prioridade=row["motivo_prioridade"],   
            )
            
            ag.id_agendamento = row["id_agendamento"]
            ag.id_fila = row["id_fila"]
            
            agendamentos.append(ag)
        
        return agendamentos 
    
    def listar_todos(self):
        con = connection()
        con.row_factory = sqlite3.Row
        cursor = con.cursor()
        
        cursor.execute("SELECT * FROM agendamento")
        rows = cursor.fetchall()
        
        con.close()
        
        return self.construir_objeto(rows)
    
    def buscar_por_cidadao(self, cidadao: Cidadao):
        con = connection()
        con.row_factory = sqlite3.Row
        cursor = con.cursor()
        
        cursor.execute("SELECT * FROM agendamento WHERE num_sus = ?", (cidadao.num_sus,))
        rows = cursor.fetchall()
        
        con.close()
        
        return self.construir_objeto(rows)
    
    def buscar_por_fila(self, fila: Fila_atendimento):
        con = connection()
        con.row_factory = sqlite3.Row
        cursor = con.cursor()
        
        cursor.execute("SELECT * FROM agendamento WHERE id_fila = ?", (fila.id_fila,))
        rows = cursor.fetchall()
        
        con.close()
        
        return self.construir_objeto(rows)
    
    def buscar_por_id(self, id_agendamento):
        con = connection()
        con.row_factory = sqlite3.Row
        cursor = con.cursor()
        
        cursor.execute("SELECT * FROM agendamento WHERE id_agendamento = ?", (id_agendamento,))
        row = cursor.fetchone()
        
        con.close()
        
        if row is None:
            return None
        
        return self.construir_objeto([row])[0]