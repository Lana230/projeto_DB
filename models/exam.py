from models.appointment import Appointment
from enum import Enum

class Type_exam(Enum):
    EXAM_LAB = "Exames laboratoriais"
    EXAM_IMA = "Exames de imagem"
    EXAM_CARD = "Exames cardiológicos"
    EXAM_PREV = "Exames preventivos"

def Exam_from_number(num):
    mapping = {
        1: Type_exam.EXAM_LAB,
        2: Type_exam.EXAM_IMA,
        3: Type_exam.EXAM_CARD,
        4: Type_exam.EXAM_PREV
    }
    return mapping.get(num)

class Exam:
    def __init__(self, Appointment, name_exam, type_num , degree_urgency):
        self.Appointment = Appointment
        self.name_exam = name_exam
        self.type = Exam_from_number(type_num)
        self.degree_urgency = degree_urgency





