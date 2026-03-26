from models import Telefone

from database.conexao import connection

class TelefoneRepository:
    
    def salvar(self, telefone: Telefone):
        con = connection()
        cursor = con.cursor()
        
        if telefone.ubs is None and telefone.pessoa is not None:
            cursor.execute("""
                INSERT INTO telefone (
                    num_telefone, id_pessoa
                ) VALUES (?, ?)
                """, (
                    telefone.num_telefone, 
                    telefone.pessoa.id_pessoa
                ))
        elif telefone.pessoa is None and telefone.ubs is not None:
            cursor.execute("""
                INSERT INTO telefone (
                    num_telefone, id_ubs
                ) VALUES (?, ?)
                """, (
                    telefone.num_telefone, 
                    telefone.ubs.id_ubs
                ))
        
        telefone.id_telefone = cursor.lastrowid
        
        con.commit()
        con.close()
        
        return telefone