from models import *
from repositories import *

from database.conexao import connection

class Medication_appoi_repository():
    def __init__(self):
        self.med_repo = Medication_repository()
        self.appoi_repo = Appointment_repository()

    #SALVAR MEDICAMENTO_CONSULTA DENTRO DO BANCO DE DADOS
    def save_medication_appoi_db(self, cursor, appointment: Appointment, medi_appoi: Medication_appoi):
        cursor.execute(
            "INSERT INTO medicamento_consulta (id_medicamento, id_consulta, frequencia_dias, duracao_adm, dose, via) VALUE (?, ?, ?, ?, ?, ?)",
            (medi_appoi.medication.id_medication, appointment.id_appointment, medi_appoi.frequency_days, medi_appoi.duraction_adm, medi_appoi.dose, medi_appoi.via)
        )
        
        return medi_appoi
    
    def build_object_med_appoi(self, rows):
        appointment_med = []

        for row in rows:
            appoi_med = Medication_appoi(
                medication = self.med_repo.search_per_id(row["id_medicamento"]),
                appointment = self.appoi_repo.search_per_id(row["id_consulta"]),
                dose = row["dose"],
                via = row["via"],
                frequency_days = row["frequencia"],
                duracao = row["duracao"],
            )

            appointment_med.append(appoi_med)

        return appointment_med