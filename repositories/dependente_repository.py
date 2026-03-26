import sqlite3
from database.conexao import connection

from models import Dependente

from .pessoa_repository import PessoaRepository

class DependenteRepository:
    def __init__(self):
        self.pessoa_repo = PessoaRepository()
    
    def salvar(self, dependente: Dependente):
        con = connection()
        cursor = con.cursor()
        
        cursor.execute("""
            INSERT INTO dependente (
                id_responsavel, id_dependente, parentesco
            ) VALUES (?, ?, ?)
        """, (
            dependente.responsavel.id_pessoa,
            dependente.dependente.id_pessoa,
            dependente.parentesco
        ))
        
        con.commit()
        con.close()
        
        return dependente
    
    def construir_objeto(self, rows):
        dependentes = []
        
        for row in rows:
            if row is None:
                continue
            
            resp = self.pessoa_repo.buscar_por_id(row["id_responsavel"])
            dep = self.pessoa_repo.buscar_por_id(row["id_dependente"])
            
            dependente = Dependente(
                responsavel=resp,
                dependente=dep,
                parentesco=row["parentesco"]
            )
            
            dependentes.append(dependente)
        
        return dependentes
    
    def listar_todos(self):
        con = connection()
        con.row_factory = sqlite3.Row
        cursor = con.cursor()
        
        cursor.execute("SELECT * FROM dependente")
        
        rows = cursor.fetchall()
        
        con.close()
        
        return self.construir_objeto(rows)
    
    def buscar_por_id(self, id_responsavel, id_dependente):
        con = connection()
        con.row_factory = sqlite3.Row
        cursor = con.cursor()
        
        cursor.execute("SELECT * FROM dependente WHERE id_responsavel = ? AND id_dependente = ?", (id_responsavel, id_dependente))
        
        row = cursor.fetchone()
        
        con.close()
        
        if row is None:
            return None
        
        return self.construir_objeto([row])[0]
    