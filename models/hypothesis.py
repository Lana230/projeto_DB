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

    
