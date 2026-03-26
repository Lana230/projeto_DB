from models.cidadao import Cidadao
from models.vaccine import Vaccine
from models.enfermeiro import Enfermeiro
from models.ubs import Ubs

class Record_vaccine:
    def __init__(self, citizen: Cidadao, vaccine_ubs: Vaccine, enfermeiro: Enfermeiro, ubs: Ubs, data):
        self.id_vaccine_record = None
        self.citizen = citizen 
        self.vaccine_ubs = vaccine_ubs
        self.nurse = enfermeiro
        self.ubs = ubs
        self.data = data

    def record(self):
        print("\n--- Registro de Vacina ---")
        print("UBS: ", self.ubs.name)
        print("Data: ", self.data.strtime("%d/%m/%Y"))
        self.vaccine.details_vaccine()
        print(f"Paciente: {self.citizen.nome} || Sus: {self.citizen.sus}") 
        print(f"Enfermeiro: {self.nurse.name} || Cip: {self.nurse.cip}") 
        print("----------------\n")
        
    