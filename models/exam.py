from .cidadao import Cidadao
from .medico import Medico
from .appointment import Appointment
from enum import Enum

from database.conexao import connection
con = connection()
cursor = con.cursor()

class Exam_Type(Enum):
    EXAM_LAB = "Exames laboratoriais"
    EXAM_IMA = "Exames de imagem"
    EXAM_CARD = "Exames cardiológicos"
    EXAM_PREV = "Exames preventivos"

class Status_exam(Enum):
    REQUESTED = "Solicitado"
    DONE = "Realizado"

class Type_degree(Enum):
    LOW = "Baixa"
    MEDIUM = "Média"
    HIGH = "Alta"

class Exam:
    def __init__(self, appointment: Appointment, name_exam, exam_type: Exam_Type, degree_urgency: Type_degree, status_exam: Status_exam):
        self.id_exam = None
        self.Appointment = appointment
        self.name_exam = name_exam
        self.type = exam_type
        self.status = status_exam
        self.degree_urgency = degree_urgency

    def add_data(self, data):
        self.data = data

    def add_result(self, result):
        self.result = result

    def details_exam(self):
        print(f"Exame: {self.name_exam} || Tipo: {self.type.value}")
        print("Grau de Urgencia: ", self.degree_urgency)
        print("Estado: ", self.status.value)
        
        if self.status == Status_exam.DONE:
            print("Data coleta:", self.data.strftime("%d/%m/%Y"))
            print("Resultado: ", self.result)