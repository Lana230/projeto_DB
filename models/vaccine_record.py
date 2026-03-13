from models.cidadao import Cidadao
from models.enfermeiro import Enfermeiro
from models.vaccine import Vaccine

class Vaccine_record:
    def __init__(self, cidadao, vaccine, enfermeiro, ubs, data):
        self.citizen = cidadao 
        self.vaccine = vaccine
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
        
