from enum import Enum

class Via_medication(Enum):
    ORAL = "Oral"
    INTRAVENOUS = "Intravenosa"
    INTRAMUSCULAR = "Intramuscular"
    SUBCUTANEOUS = "Subcutânea"
    NASAL = "Nasal"
    TOPICA = "Tópica"

class Medication:
    def __init__(self, name, dose, via : Via_medication, frequency_days, duraction_adm):
        self.name = name
        self.dose = dose
        self.via = via
        self.frequency_days = frequency_days
        self.duraction_adm = duraction_adm

    def details_medication(self):
        print("Nome Generico: ", self.name)
        print(f"Dose: {self.dose} || Via: {self.via}")
        print("Frequencia por dia: ", self.frequency_days)
        print("Duracao: ", self.duraction_adm)


    