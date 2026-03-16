from .cidadao import Cidadao
from .medico import Medico
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

class Medication:
    def __init__(self, appointment: Appointment, citizen: Cidadao, doctor: Medico, name_medication, dose, via : Via_medication, frequency_days, duraction_adm):
        self.id_medication = None
        self.citizen = citizen
        self.doctor = doctor
        self.appointment = appointment
        self.name_medication = name_medication
        self.dose = dose
        self.via = via
        self.frequency_days = frequency_days
        self.duraction_adm = duraction_adm

    def details_medication(self):
        print("Nome Generico: ", self.name_medication)
        print(f"Dose: {self.dose} || Via: {self.via}")
        print("Frequencia por dia: ", self.frequency_days)
        print("Duracao: ", self.duraction_adm)
    
    #SALVAR MEDICAMENTOS DENTRO DO BANCO DE DADOS
    def save_medication_db(self, id_appointment):
        cursor.execute(
            "INSERT INTO medicamentos (id_consulta, id_cidadao, id_medico, name_medicamento, dose, via, frequencia_dias, duracao_adm) VALUE (?, ?, ?, ?, ?, ?, ?, ?)",
            (id_appointment, self.citizen.num_sus, self.doctor.crm, self.name_medication, self.dose, self.via, self.frequency_days, self.duraction_adm)
        )

        self.id_medication = cursor.lastrowid


    