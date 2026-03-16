from models import *

from database.conexao import connection

class AnamneseRepository():
    def salvar_anamnese(self, anamnese):
        con = connection()
        cursor = con.cursor()
        
        cursor.execute(
            "INSERT INTO anamnese (num_sus, id_consulta, peso, altura, pressao_arterial) VALUES (?, ?, ?, ?, ?)", (anamnese.cidadao.num_sus, anamnese.appointment.id_appointment, anamnese.peso, anamnese.altura, anamnese.pressao_arterial)
        )
        
        self.id_anamnese = cursor.lastrowid
        
        con.commit()
        con.close()

    def buscar_todos(self):
        con = connection()
        cursor = con.cursor()
        
        cursor.execute(
            "SELECT * FROM anamnese"
        )
        
        anamneses = cursor.fetchall()
        
        con.close()
        
        return anamneses
    
    def buscar_por_cidadao(self, cidadao: Cidadao):
        con = connection()
        cursor = con.cursor()
        
        cursor.execute(
            "SELECT * FROM anamnese WHERE num_sus = ?", (cidadao.num_sus)
        )
        
        anamnese = cursor.fetchall()
        
        con.close()
        
        return anamnese
    
    def buscar_por_id(self, id_anamnese):
        con = connection()
        cursor = con.cursor()
        
        cursor.execute(
            "SELECT * FROM anamnese WHERE id_anamnese = ?", (id_anamnese)
        )