from .medication import Medication
from .appointment import Appointment
from enum import Enum

class Via_medication(Enum):
    ORAL = "Oral"
    INTRAVENOUS = "Intravenosa"
    INTRAMUSCULAR = "Intramuscular"
    SUBCUTANEOUS = "Subcutânea"
    NASAL = "Nasal"
    TOPICA = "Tópica"

class Medication_appoi():
    def __init__(self, medication: Medication, appointment: Appointment, dose, via : Via_medication, frequency_days, duraction_adm):
        self.medication = medication 
        self.appointment = appointment
        self.dose = dose
        self.via = via
        self.frequency_days = frequency_days
        self.duraction_adm = duraction_adm

    def details_medication(self):
        print("Nome Generico: ", self.name_medication)
        print(f"Dose: {self.dose} || Via: {self.via}")
        print("Frequencia por dia: ", self.frequency_days)
        print("Duracao: ", self.duraction_adm)