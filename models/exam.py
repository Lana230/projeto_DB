from enum import Enum

class Type_exam(Enum):
    EXAM_LAB = "Exames laboratoriais"
    EXAM_IMA = "Exames de imagem"
    EXAM_CARD = "Exames cardiológicos"
    EXAM_PREV = "Exames preventivos"

class Status_exam(Enum):
    REQUESTED = "Solicitado"
    SCHEDULED = "Agendado"
    IN_PROGRESS = "Em andamento"
    DONE = "Realizado"
    CANCELED = "Cancelado"

class Type_degree(Enum):
    LOW = "Baixa"
    MEDIUM = "Média"
    HIGH = "Alta"

class Exam:
    def __init__(self, appointment, name_exam, type_exam: Type_exam, degree_urgency: Type_degree, status_exam: Status_exam):
        self.Appointment = appointment
        self.name_exam = name_exam
        self.type = type_exam
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
        
        if self.status == Status_exam.SCHEDULED:
            print("Data agendada:", self.data.strftime("%d/%m/%Y"))
       
        if self.status == Status_exam.DONE:
            print("Data coleta:", self.data.strftime("%d/%m/%Y"))
            print("Resultado: ", self.result)
    

