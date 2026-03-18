from models import *

from database.conexao import connection

class Hypothesis_repository():
    #SALVAR HIPOTESES BANCO DE DADOS
    def save_hypothesis_db(self, appointment: Appointment, hypothesis: Hypothesis):
        cursor.execute(
            "INSERT INTO hipotese (id_consulta, doenca, cid) VALUE (?, ?, ?)",
            (appointment.id_appointment, hypothesis.disease, hypothesis.cid)
        )

        hypothesis.id_hypothesis = cursor.lastrowid
        
        return hypothesis