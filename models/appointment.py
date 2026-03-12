#importacion
from models.cidadao import Cidadao
#from doctor import Doctor(medico)
from models.exam import Exam
from models.ubs import Ubs
from datetime import date

#class
class Appointment:
    def __init__(self, Cidadao, Doctor, Ubs, data, reason, conclusion):
        self.cidadao = Cidadao
        self.doctor = Doctor
        self.Ubs = Ubs
        self.data = data
        self.reason = reason
        self.conclusion = conclusion
        self.exam = []

    def add_exam(self, exam):
        self.exam.append(exam)

    def show_exams(self):
        for exam in self.exam:
            exam.details_exam()

    def details_appoi(self):
        print("\n--- Consulta ---")
        print("UBS: ", self.Ubs.name)
        print(f"Paciente: {self.cidadao.nome} || Numero do Sus: {self.cidadao.sus}") #adicione aqui a ligacao com cidadao
        print(f"Medico: {self.Doctor.name} || Numero do CRM: {self.Doctor.crm}") #adicione aqui a ligacao com medico
        print("Data: ", self.data.strtime("%d/%m/%Y"))
        print("Motivo: ", self.reason)
        print("Conclusao ", self.conclusion)
        print("\n--- Exames ---")
        self.show_exams()
        print("----------------\n")