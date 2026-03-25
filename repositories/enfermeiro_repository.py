import sqlite3
from models import Enfermeiro, Ubs
from .ubs_repository import Ubs_repository
from .pessoa_repository import PessoaRepository
from database.conexao import connection

class EnfermeiroRepository:
    
    def __init__(self):
        self.pessoa_repo = PessoaRepository()
        self.ubs_repo = Ubs_repository()
    
    def salvar(self, enfermeiro: Enfermeiro):
        con  = connection()
        cursor = con.cursor()
        
        if enfermeiro.id_pessoa is None:
            pessoa = self.pessoa_repo.salvar(enfermeiro)
            enfermeiro.id_pessoa = pessoa.id_pessoa
        
        cursor.execute("""
            INSERT INTO enfermeiro (
                cip, id_pessoa
            ) VALUES (?, ?)
            """, (
                enfermeiro.cip,
                enfermeiro.id_pessoa
            ))
        
        con.commit()
        con.close()
        
        return enfermeiro
    
    def construir_objeto(self, rows):
        enfermeiros = []
        
        for row in rows:
            if row is None:
                continue
            
            ubs = self.ubs_repo.search_per_id(row["id_ubs"])
            
            enfermeiro = Enfermeiro(
                nome_pessoa=row["nome_pessoa"],
                estado_civil=row["estado_civil"],
                ubs=ubs,
                cip=row["cip"]
            )
            
            enfermeiro.id_pessoa = row["id_pessoa"]
            
            enfermeiros.append(enfermeiro)
        
        return enfermeiros
    
    def listar_enfermeiros_por_ubs(self, ubs: Ubs):
        con = connection()
        con.row_factory = sqlite3.Row
        cursor = con.cursor()

        cursor.execute("""
            SELECT 
                p.id_pessoa, p.nome_pessoa, p.id_ubs, p.estado_civil, 
                e.cip 
            FROM pessoa p INNER JOIN enfermeiro e ON p.id_pessoa = e.id_pessoa WHERE p.id_ubs = ?
            """, (ubs.id_ubs,)
        )
        
        rows = cursor.fetchall()
        
        con.close()
        
        return self.construir_objeto(rows)
    
    #adicionar procurar por id pra colocar em registro de vacina