from models import *

from database.conexao import connection

class Exam_repository():
    #SALVAR EXAMES DENTRO DO BANCO DE DADOS
    def save_exam_db(self, appointment: Appointment, exam: Exam):
        cursor.execute(
            "INSERT INTO exame (id_consulta, nome_exame, tipo_exame, grau_urgencia, status_exame) VALUE (?, ?, ?, ?, ?)",
            (appointment.id_appointment, exam.name_exam, exam.type, exam.degree_urgency, exam.status)
        )

        exam.id_exam = cursor.lastrowid
        
        return exam
    
