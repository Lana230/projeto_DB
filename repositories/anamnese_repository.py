import sqlite3
from models import Anamnese, Cidadao
from database.conexao import connection

class AnamneseRepository():
    
    def salvar(self, anamnese: Anamnese):
        con = connection()
        cursor = con.cursor()
        
        cursor.execute("""
            INSERT INTO anamnese (
                num_sus, peso, altura, 
                data_anamnese, pressao_arterial
                ) VALUES (?, ?, ?, ?, ?)
                """, (
                    anamnese.cidadao.num_sus,  
                    anamnese.peso, 
                    anamnese.altura,
                    anamnese.data_anamnese, 
                    anamnese.pressao_arterial
            ))
        
        anamnese.id_anamnese = cursor.lastrowid
        
        con.commit()
        con.close()
        
        return anamnese
    
    def construir_objeto(self, rows):
        anamneses = []
        
        for row in rows:
            if row is None:
                continue
            
            an = Anamnese(
                cidadao=None, #depois buscar no repositorio de cidadao
                data_anamnese=row["data_anamnese"],
                peso=row["peso"],
                altura=row["altura"],
                pressao_arterial=row["pressao_arterial"]
            )
            
            an.id_anamnese = row["id_anamnese"]
            
            anamneses.append(an)
        
        return anamneses

    def listar_todos(self):
        con = connection()
        con.row_factory = sqlite3.Row
        cursor = con.cursor()
        
        cursor.execute(
            "SELECT * FROM anamnese"
        )
        rows = cursor.fetchall()
        
        con.close()
        
        return self.construir_objeto(rows)
    
    def buscar_por_cidadao(self, cidadao: Cidadao):
        con = connection()
        con.row_factory = sqlite3.Row
        cursor = con.cursor()
        
        cursor.execute(
            "SELECT * FROM anamnese WHERE num_sus = ?", (cidadao.num_sus,)
        )
        rows = cursor.fetchall()
        
        con.close()
        
        return self.construir_objeto(rows)
    
    def buscar_por_id(self, id_anamnese):
        con = connection()
        con.row_factory = sqlite3.Row
        cursor = con.cursor()
        
        cursor.execute(
            "SELECT * FROM anamnese WHERE id_anamnese = ?", (id_anamnese,)
        )
        
        row = cursor.fetchone()
        
        con.close()
        
        if row is None:
            return None
        
        return self.construir_objeto([row])[0]