from .cidadao import Cidadao
from .appointment import Appointment

from database.conexao import connection
con = connection()
cursor = con.cursor()

class Hypothesis:
    def __init__(self, appointment: Appointment, disease, cid):
        self.id_hypothesis = None
        self.appointment = appointment
        self.disease = disease
        self.cid = cid

    def show_hypothesis_cid(self):
        print(f"{self.disease} || CID: {self.cid}")

    #SALVAR HIPOTESES BANCO DE DADOS
    def save_hypothesis_db(self, id_appointment):
        cursor.execute(
            "INSERT INTO hipotese (id_consulta, doencan, cid) VALUE (?, ?, ?)",
            (id_appointment, self.disease, self.cid)
        )

        self.id_hypothesis = cursor.lastrowid
