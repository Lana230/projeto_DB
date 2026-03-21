#importacion
from models.ubs import Ubs
from models.cidadao import Cidadao
from models.medico import Medico
from models.exam import Exam
from .medication_appoi import Medication_appoi
from models.hypothesis import Hypothesis
from datetime import date

from database.conexao import connection
con = connection()
cursor = con.cursor()

#class
class Appointment:
    def __init__(self, citizen: Cidadao, doctor: Medico, ubs: Ubs, date, reason, life_habits):
        self.id_appointment = None
        self.citizen = citizen
        self.doctor = doctor
        self.ubs = ubs
        self.date = date
        self.reason = reason
        self.life_habits = life_habits
        self.hypothesis = [] 
        self.exam = [] 
        self.medication_appoi = []

    def add_hypothesis(self, hypothesis: Hypothesis):
        self.hypothesis.append(hypothesis)
    
    def show_hypothesis(self):
        for hypothesis in self.hypothesis:
            hypothesis.show_hypothesis_cid()

    def add_exam(self, exam: Exam):
        self.exam.append(exam)
    
    def show_exams_names(self):
        for exam in self.exam:
            print(f"- {exam.name_exam} || {exam.type}")
    
    def add_medication(self, medication_appoi: Medication_appoi):
        self.medication_appoi.append(medication_appoi)

    def show_medication(self):
        for medication in self.medication_appoi:
            medication.details_medication()

    def reg_appointment(self):
        print("\n--- Informacoes Gerais ---")
        print("UBS: ", self.ubs.name)
        print("Data: ", self.data.strftime("%d/%m/%Y"))
        print("\n--- Dados do Paciente ---")
        self.citizen.exibir()
        print("\n--- Dados do Medico Responsavel ---")
        print(f"Medico: {self.doctor.name} || Numero do CRM: {self.doctor.crm}")
        print("Motivo: ", self.reason)
        print("Habitos de vida:", self.life_habits)
        self.hypothesis.show_hypothesis_cid()
        print("\n--- Exames ---")
        self.show_exams_names()
        print("\n--- Medicamentos ---")
        self.show_medication()
        print("----------------\n")

    #CONSULTAS DO BANDO DE DADOS
    def search_all(self):
        cursor.execute(
            "SELECT * FROM consulta WHERE crm = ?",
            (self.doctor.crm,)
        )

        return cursor.fetchall()
    
    def search_per_data(self, data: date):
        cursor.execute(
            "SELECT * FROM consulta WHERE data = ?",
            (data.isoformat(),)
        )

        return cursor.fetchall()

    def search_per_citizen(self, sus_pacient):
        cursor.execute(
            "SELECT * FROM consulta WHERE sus = ?",
            (sus_pacient,)
        )

        return cursor.fetchall()