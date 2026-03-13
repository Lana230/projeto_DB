#importacion
from models.ubs import Ubs
from models.cidadao import Cidadao
from models.medico import Medico
from models.exam import Exam
from models.medication import Medication
from datetime import date

#class
class Appointment:
    def __init__(self, cidadao, medico, Ubs, data, reason, hypothesis):
        self.citizen = cidadao
        self.doctor = medico
        self.Ubs = Ubs
        self.data = data
        self.reason = reason #subjetivo
        self.hypothesis = hypothesis #avaliacao
        self.exam = [] #objetivo
        self.medication = []

    def add_exam(self, exam):
        self.exam.append(exam)
    
    def show_exams_names(self):
        for exam in self.exam:
            print(f"- {exam.name_exam} || {exam.type}")
    
    def add_medication(self, medication):
        self.medication.append(medication)

    def show_medication(self):
        for medication in self.medication:
            medication.details_medication()

    def reg_appointment(self):
        print("\n--- Informacoes Gerais ---")
        print("UBS: ", self.Ubs.name)
        print("Data: ", self.data.strftime("%d/%m/%Y"))
        print("\n--- Dados do Paciente ---")
        self.citizen.exibir()
        print("\n--- Dados do Medico Responsavel ---")
        print(f"Medico: {self.doctor.name} || Numero do CRM: {self.doctor.crm}")
        print("Motivo: ", self.reason)
        print("Conclusao ", self.hypothesis)
        print("\n--- Exames ---")
        self.show_exams_names()
        print("\n--- Medicamentos ---")
        self.show_medication()
        print("----------------\n")