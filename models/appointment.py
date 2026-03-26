#importacion
from models.ubs import Ubs
from models.agendamento import Agendamento
from models.medico import Medico
from models.exam import Exam
from .medication_appoi import Medication_appoi
from models.hypothesis import Hypothesis
from models.fila_atendimento import Fila_atendimento, TipoAtendimento, StatusAgendamento
from repositories.ubs_repository import Ubs_repository
from repositories.agendamento_repository import AgendamentoRepository
from datetime import date


from database.conexao import connection
con = connection()
cursor = con.cursor()

'''Problema de fluxo circular entre exam e appointment'''

#class
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

    def schedule_an_appointment(self, service_line: Fila_atendimento):
        if service_line.tipo_atendimento != TipoAtendimento.CONSULTA:
            raise ValueError("A linha de atendimento deve ser do tipo consulta para agendar uma consulta")

        if (self.doctor.crm != service_line.doctor.crm) and (self.ubs.id_ubs != service_line.ubs.id_ubs):
            raise ValueError("O médico da consulta deve ser o mesmo da linha de atendimento e a UBS da consulta deve ser a mesma da linha de atendimento")
        
        for scheduling in service_line.agendamentos:
            if scheduling.id_agendamento == self.scheduling.id_agendamento:
                AgendamentoRepository().atualizar_status(scheduling, StatusAgendamento.CONCLUIDO)
                break

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

