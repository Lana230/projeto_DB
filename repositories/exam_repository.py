import sqlite3
from database.conexao import connection

from models.appointment import Appointment
from models.exam import Exam

from .appointment_repository import Appointment_repository

class Exam_repository():
    def __init__(self):
        self.appoi_repo = Appointment_repository()

    #SALVAR EXAMES DENTRO DO BANCO DE DADOS
    def save_exam_db(self, cursor,appointment: Appointment, exam: Exam):
        con = connection()
        cursor = con.cursor()
        
        cursor.execute(
            "INSERT INTO exame (id_consulta, nome_exame, tipo_exame, grau_urgencia, status_exame) VALUE (?, ?, ?, ?, ?)",
            (appointment.id_appointment, exam.name_exam, exam.type, exam.degree_urgency, exam.status)
        )

        exam.id_exam = cursor.lastrowid
        
        con.commit()
        con.close()
        
        return exam
    
    def build_object_exam(self, rows):
        exams = []

        for row in rows:
            if row is None:
                continue

            exam = Exam(
                appointment = self.appoi_repo.search_per_id(row["id_consulta"]),
                name_exam = row["nome"],
                exam_type = row["tipo"],
                degree_urgency = row["grau_urgencia"],
                status_exam = row["status"],
            )

            exam.id_exam = row["id_exame"]

            exams.append(exam)

        return exams   

    def search_per_id(self, id_exam):
        con = connection()
        con.row_factory = sqlite3.Row
        cursor = con.cursor()

        cursor.execute(
            "SELECT * FROM exame WHERE id_exame = ?",
            (id_exam,)
        )
        row = cursor.fetchone()

        con.close()

        if row is None:
            return None

        return self.build_object_exam([row])[0]