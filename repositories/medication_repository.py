import sqlite3
from database.conexao import connection

from models import Medication

class Medication_repository():
    #Salvar 
    def save(self, medication: Medication):
        con = connection()
        cursor = con.cursor()
        
        try:
            cursor.execute(
                "INSERT INTO medicamentos(nome_medicamento) VALUES (?)",
                (medication.name_medication)
            )

            medication.id_medication = cursor.lastrowid
            con.commit()

        except Exception as e:
            con.rollback() 
            print("Erro:", e)

        finally:
            con.close()

        return medication
    
    #construir objeto
    def build_object(self, rows):
        medications = []

        for row in rows:
            if row is None:
                continue

            medication = Medication(
                name_medication = row["nome_medicamento"],
            )

            medication.id_medication = row["id_medicamento"]

            medications.append(medication)

        return medications
    
    def search_per_id(self, id_medication):
        con = connection()
        con.row_factory = sqlite3.Row
        cursor = con.cursor()

        cursor.execute(
            "SELECT * FROM medicamento WHERE id_medicamento = ?", 
            (id_medication,)
        )

        row = cursor.fetchone()

        con.close()

        if row is None:
            return None
        
        return self.build_object([row])[0]