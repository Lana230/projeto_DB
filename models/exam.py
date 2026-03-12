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

class Exam:
    def __init__(self, appointment, name_exam, type_exam , degree_urgency, status_exam):
        self.Appointment = appointment
        self.name_exam = name_exam
        self.type = type_exam
        self.status = status_exam
        self.degree_urgency = degree_urgency

    def details_exam(self):
        print(f"Exame: {self.name_exam} || Tipo: {self.type.value}")
        print("Grau de Urgencia: ", self.degree_urgency)
        print("Estado: ", self.status.value)
        if(self.status.value == Status_exam.SCHEDULED.value):
            print("Data: ")
    

