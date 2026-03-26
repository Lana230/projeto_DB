import sqlite3
from database.conexao import connection

from models.medico import Medico
from models.ubs import Ubs

from .ubs_repository import Ubs_repository
from .pessoa_repository import PessoaRepository

class MedicoRepository:
    
    def __init__(self):
        self.pessoa_repo = PessoaRepository()
        self.ubs_repo = Ubs_repository()
    
    def salvar(self, medico: Medico):
        con = connection()
        cursor = con.cursor()
        
        if medico.id_pessoa is None:
            pessoa = self.pessoa_repo.salvar(medico)
            medico.id_pessoa = pessoa.id_pessoa
        
        cursor.execute("""
            INSERT INTO medico (
                crm, especialidade, id_pessoa
            ) VALUES (?, ?, ?)              
            """, (
                medico.crm, 
                medico.especialidade, 
                medico.id_pessoa
            ))
        
        con.commit()
        con.close()
        
        return medico
    
    def construir_objeto(self, rows):
        medicos = []
        
        for row in rows:
            if row is None:
                continue
            
            ubs = self.ubs_repo.search_per_id(row["id_ubs"])
            
            medico = Medico(
                nome_pessoa=row["nome_pessoa"],
                estado_civil=row["estado_civil"],
                ubs=ubs,
                crm=row["crm"],
                especialidade=row["especialidade"]
            )

            medico.id_pessoa = row["id_pessoa"]
            
            medicos.append(medico)
        
        return medicos
        
    
    def listar_medicos_por_ubs(self, ubs: Ubs):
        con = connection()
        con.row_factory = sqlite3.Row
        cursor = con.cursor()

        cursor.execute("""
            SELECT 
                p.id_pessoa, p.nome_pessoa, p.id_ubs, p.estado_civil, 
                m.crm, m.especialidade 
            FROM pessoa p INNER JOIN medico m ON p.id_pessoa = m.id_pessoa WHERE p.id_ubs = ?
            """, (ubs.id_ubs,)
        )
        
        rows = cursor.fetchall()
        
        con.close()
        
        return self.construir_objeto(rows)
    
    def buscar_por_crm(self, crm):
        con = connection()
        con.row_factory = sqlite3.Row
        cursor = con.cursor()
        
        cursor.execute("""
            SELECT
                p.id_pessoa, p.nome_pessoa, p.id_ubs, p.estado_civil,
                m.crm, m.especialidade
            FROM pessoa p INNER JOIN medico m ON p.id_pessoa = m.id_pessoa WHERE m.crm = ?
            """, (crm,)
        )
        
        row = cursor.fetchone()
        
        con.close()
        
        if row is None:
            return None
        
        return self.construir_objeto([row])[0]