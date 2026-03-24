from models import Grupo_vulneravel
from database.conexao import connection

class Grupo_vulneravel_Repository:
    
    def salvar(self, grupo_vulneravel: Grupo_vulneravel):
        con = connection()
        cursor = con.cursor()
        
        cursor.execute("""
            INSERT INTO grupo_vulneravel (
                nome_grupo, peso_prioridade, descricao
            ) VALUES (?, ?, ?)
            """, (
                grupo_vulneravel.nome_grupo.value,
                grupo_vulneravel.peso_prioridade,
                grupo_vulneravel.descricao
            ))
        
        grupo_vulneravel.id_grupo = cursor.lastrowid
        con.commit()
        con.close()
        
        return grupo_vulneravel