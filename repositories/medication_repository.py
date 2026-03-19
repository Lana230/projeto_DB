from models import *

from database.conexao import connection

class Medication_repository():
    def save_medication_db(self, medication: Medication):
        con = connection()
        cursor = con.cursor()
        
        try:
            cursor.execute(
                "INSERT INTO medicamentos(nome_medicamento, categoria_med) VALUES (?, ?)",
                (medication.name_medication, medication.category_med)
            )

            medication.id_medication = cursor.lastrowid
            con.commit()

        except Exception as e:
            con.rollback() 
            print("Erro:", e)

        finally:
            con.close()

        return medication