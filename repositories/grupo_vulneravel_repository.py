import sqlite3
from database.conexao import connection

from models.grupo_vulneravel import Grupo_vulneravel, NomeGrupo

class Grupo_vulneravel_repository:
    
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
    
    def construir_objeto(self, rows):
        grupos = []
        
        for row in rows:
            if row is None:
                continue
            
            grupo = Grupo_vulneravel(
                nome_grupo=NomeGrupo(row["nome_grupo"]),
                peso_prioridade=row["peso_prioridade"],
                descricao=row["descricao"]
            )
            
            grupo.id_grupo = row["id_grupo"]
            
            grupos.append(grupo)
        
        return grupos
    
    def listar_todos(self):
        con = connection()
        con.row_factory = sqlite3.Row
        cursor = con.cursor()
        
        cursor.execute("SELECT * FROM grupo_vulneravel")
        
        rows = cursor.fetchall()
        
        con.close()
        
        return self.construir_objeto(rows)
    
    def buscar_por_id(self, id_grupo):
        con = connection()
        con.row_factory = sqlite3.Row
        cursor = con.cursor()
        
        cursor.execute("SELECT * FROM grupo_vulneravel WHERE id_grupo = ?", (id_grupo,))
        
        row = cursor.fetchone()
        
        con.close()
        
        if row is None:
            return None
        
        return self.construir_objeto([row])[0]