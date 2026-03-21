from models import Pessoa
from database.conexao import connection
from .ubs_repository import Ubs_repository

class PessoaRepository():
    
    def __init__(self):
        self.ubs_repo = Ubs_repository()
    
    def salvar(self, pessoa: Pessoa):
        con = connection()
        cursor = con.cursor()
        
        cursor.execute("""
            INSERT INTO pessoa (
                nome_pessoa, id_ubs, estado_civil
            ) VALUES (?, ?, ?)
            """, (
                pessoa.nome_pessoa,
                pessoa.ubs.id_ubs,
                pessoa.estado_civil
            ))
        
        pessoa.id_pessoa = cursor.lastrowid
        
        con.commit()
        con.close()
        
        return pessoa
    
    def construir_objeto(self, rows):
        pessoas = []
        
        for row in rows:
            if row is None:
                continue
            
            ubs = self.ubs_repo.search_per_id(row["id_ubs"])
            
            pessoa = Pessoa(
                nome_pessoa=row["nome_pessoa"],
                estado_civil=row["estado_civil"],
                ubs=ubs
            )
            
            pessoa.id_pessoa = row["id_pessoa"]
            
            pessoas.append(pessoa)
        
        return pessoas