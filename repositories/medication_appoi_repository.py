from models import *

from database.conexao import connection

class Medication_appoi_repository():
    #SALVAR MEDICAMENTO_CONSULTA DENTRO DO BANCO DE DADOS
    def save_medication_appoi_db(self, cursor, appointment: Appointment, medi_appoi: Medication_appoi):
        cursor.execute(
            "INSERT INTO medicamento_consulta (id_medicamento, id_consulta, frequencia_dias, duracao_adm, dose, via) VALUE (?, ?, ?, ?, ?, ?)",
            (medi_appoi.medication.id_medication, appointment.id_appointment, medi_appoi.frequency_days, medi_appoi.duraction_adm, medi_appoi.dose, medi_appoi.via)
        )

        medi_appoi.id_medication_appoi = cursor.lastrowid
        
        return medi_appoi