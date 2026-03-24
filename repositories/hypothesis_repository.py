from models import *
from repositories import *
from database.conexao import connection

class Hypothesis_repository():
    def __init__(self):
        self.appoi_repo = Appointment_repository()

    #SALVAR HIPOTESES BANCO DE DADOS
    def save_hypothesis_db(self, cursor, appointment: Appointment, hypothesis: Hypothesis):
        cursor.execute(
            "INSERT INTO hipotese (id_consulta, doenca, cid) VALUE (?, ?, ?)",
            (appointment.id_appointment, hypothesis.disease, hypothesis.cid)
        )

        hypothesis.id_hypothesis = cursor.lastrowid
        
        return hypothesis
    
    #CONSTRUTOR DE OBJETO
    def build_object_hypo(self, rows):
        hypothesis = []

        for row in rows:
            if row is None:
                continue
            
            hypot = Hypothesis(
                appointment = self.appoi_repo.search_per_id(row["id_consulta"]),
                disease = row["doenca"],
                cid = row["cid"],
            )

            hypot.id_hypothesis = row["id_hipotese"]

            hypothesis.append(hypot)
        
        return hypothesis
