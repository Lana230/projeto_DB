#importacion
from models.ubs import Ubs
from models.agendamento import Agendamento
from models.medico import Medico

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .exam import Exam
    from .medication_appoi import Medication_appoi
    from models.hypothesis import Hypothesis

class Appointment:
    def __init__(self, scheduling: Agendamento, doctor: Medico, ubs: Ubs, date, reason, life_habits):
        self.id_appointment = None
        self.scheduling = scheduling
        self.doctor = doctor
        self.ubs = ubs
        self.data = date
        self.reason = reason
        self.life_habits = life_habits
        self.hypothesis = [] 
        self.exam = [] 
        self.medication_appoi = []

    def add_hypothesis(self, hypothesis: "Hypothesis"):
        self.hypothesis.append(hypothesis)
    
    def show_hypothesis(self):
        for hypothesis in self.hypothesis:
            hypothesis.show_hypothesis_cid()

    def add_exam(self, exam: "Exam"):
        self.exam.append(exam)
    
    def show_exams_names(self):
        for exam in self.exam:
            print(f"- {exam.name_exam} || {exam.type}")
    
    def add_medication(self, medication_appoi: "Medication_appoi"):
        self.medication_appoi.append(medication_appoi)

    def show_medication(self):
        for medication in self.medication_appoi:
            medication.details_medication()

    def reg_appointment(self):
        print("\n--- Informacoes Gerais ---")
        print("UBS: ", self.ubs.name)
        print("Data: ", self.data.strftime("%d/%m/%Y"))
        print("\n--- Dados do Paciente ---")
        self.scheduling.exibir()
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