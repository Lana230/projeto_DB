from models import *

from database.conexao import connection

class Medication_appoi_repository():
    #SALVAR MEDICAMENTO_CONSULTA DENTRO DO BANCO DE DADOS
    def save_medication_appoi_db(self, appointment: Appointment, medi_appoi: Medication_appoi):
        cursor.execute(
            "INSERT INTO medicamento_consulta (id_consulta, id_medicamento, name_medicamento, categoria_med, dose, via, frequencia_dias, duracao_adm) VALUE (?, ?, ?, ?, ?, ?, ?, ?)",
            (appointment.id_appointment, medi_appoi.id_medication, medi_appoi.name_appoi_med, medi_appoi.cat_appoi_med, medi_appoi.dose, medi_appoi.via, medi_appoi.frequency_days, medi_appoi.duraction_adm)
        )

        medi_appoi.id_medication_appoi = cursor.lastrowid
        
        return medi_appoi