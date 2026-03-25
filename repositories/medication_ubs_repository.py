from models import *
from repositories import *

from database.conexao import connection

class Medication_ubs_repository():
    def __init__(self):
        self.medi_repo = Medication_repository()
        self.ubs_repo = Ubs_repository()

    #SALVAR MEDICAMENTO UBS NO BANCO DE DADOS
    def save(self, medication: Medication, medi_ubs : Medication_ubs):
        con = connection()
        cursor = con.cursor()

        try:
            if medication and medication.id_medication is None:
                medication = self.medi_repo.save(medication)

            cursor.execute(
                "INSERT INTO medicamento_ubs(id_medicamento, id_ubs, num_lote, quantidade_disponivel, validade) VALUES (?, ?, ?, ?, ?)",
                (medication.id_medication, medi_ubs.ubs.id_ubs, medi_ubs.num_lote, medi_ubs.available_quantity, medi_ubs.validity)
            )
            
            medi_ubs.id_medication_ubs = cursor.lastrowid
            con.commit()

        except Exception as e:
            con.rollback() 
            print("Erro:", e)

        finally:
            con.close()

        return medi_ubs
    
    #construir objeto
    def build_object(self, rows):
        medication_ubs = []

        for row in rows:

            med_ubs = Medication_ubs(
                medication = self.medi_repo.search_per_id(row["id_medicamento"]),
                ubs = self.ubs_repo.search_per_id(row["id_ubs"]),
                num_lote = row["num_lote"],
                available_quantity = row["quantidade_disponivel"],
                validity = row["validade"],
            )

            med_ubs.id_medication_ubs = row["id_medicamento_ubs"]

            medication_ubs.append(med_ubs)

        return medication_ubs