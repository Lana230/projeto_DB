from .medication import Medication
from .appointment import Appointment
from enum import Enum

from database.conexao import connection
con = connection()
cursor = con.cursor()

class Via_medication(Enum):
    ORAL = "Oral"
    INTRAVENOUS = "Intravenosa"
    INTRAMUSCULAR = "Intramuscular"
    SUBCUTANEOUS = "Subcutânea"
    NASAL = "Nasal"
    TOPICA = "Tópica"

class Medication_appoi(Medication):
    def __init__(self, name_medication, category_med, appointment: Appointment, dose, via : Via_medication, frequency_days, duraction_adm):
        self.id_medication_appoi = None
        super.__init__(name_medication, category_med)
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
    
    #SALVAR MEDICAMENTO_CONSULTA DENTRO DO BANCO DE DADOS
    def save_medication_appoi_db(self, id_appointment):
        
        super().save_medication_db()

        cursor.execute(
            "INSERT INTO medicamento_consulta (id_consulta, id_medicamento, dose, via, frequencia_dias, duracao_adm) VALUE (?, ?, ?, ?, ?, ?)",
            (id_appointment, self.id_medication, self.dose, self.via, self.frequency_days, self.duraction_adm)
        )

        self.id_medication_appoi = cursor.lastrowid


    