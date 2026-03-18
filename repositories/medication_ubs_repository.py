from models import *

from database.conexao import connection

class Medication_ubs_repository():
    #SALVAR MEDICAMENTO UBS NO BANCO DE DADOS
    def save_medication_ubs_db(self, medication: Medication, medi_ubs : Medication_ubs):
        con = connection()
        cursor = con.cursor()

        try:
            cursor.execute(
                "INSERT INTO medicamento_ubs(id_medicamento, id_ubs, num_lote, quantidade_disponivel, validade) VALUES (?, ?, ?, ?, ?)",
                (medication.id_medication, medi_ubs.ubs.id_ubs, medi_ubs.num_lote, medi_ubs.available_quantity, medi_ubs.validity)
            )
            
            medi_ubs.id_medication_ubs = cursor.lastrowid
            con.commit()

        finally:
            con.close()

        return medi_ubs