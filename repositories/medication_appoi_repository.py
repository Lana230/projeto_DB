import sqlite3
from database.conexao import connection

from models.appointment import Appointment
from models.medication_appoi import Medication_appoi

from .medication_repository import Medication_repository
from .appointment_repository import Appointment_repository

class Medication_appoi_repository():
    def __init__(self):
        self.med_repo = Medication_repository()
        self.appoi_repo = Appointment_repository()

    #SALVAR MEDICAMENTO_CONSULTA DENTRO DO BANCO DE DADOS
    def save(self, cursor, appointment: Appointment, medi_appoi: Medication_appoi):
        con = connection()
        cursor = con.cursor()
        
        cursor.execute(
            "INSERT INTO medicamento_consulta (id_medicamento, id_consulta, frequencia_dias, duracao_adm, dose, via) VALUE (?, ?, ?, ?, ?, ?)",
            (medi_appoi.medication.id_medication, appointment.id_appointment, medi_appoi.frequency_days, medi_appoi.duraction_adm, medi_appoi.dose, medi_appoi.via)
        )
        
        con.commit()
        con.close()
        
        return medi_appoi
    
    def build_object(self, rows):
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
    
    def search_per_id(self, id_medicamento, id_consulta):
        con = connection()
        con.row_factory = sqlite3.Row
        cursor = con.cursor()

        cursor.execute(
            "SELECT * FROM medicamento_consulta WHERE id_medicamento = ? AND id_consulta = ?",
            (id_medicamento, id_consulta)
        )
        row = cursor.fetchone()

        con.close()

        if row is None:
            return None

        return self.build_object([row])[0]