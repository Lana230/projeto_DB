from cidadao import Cidadao
#from nurse import Nurse (enfermeiro)
from models.vaccine import Vaccine

class Vaccine_record:
    def __init__(self, Cidadao, Vaccine, Nurse, Ubs, data):
        self.citizen = Cidadao 
        self.vaccine = Vaccine
        self.nurse = Nurse #enfermeiro
        self.ubs = Ubs
        self.data = data

    def record(self):
        print("\n--- Registro de Vacina ---")
        print("UBS: ", self.ubs.name)
        print("Data: ", self.data.strtime("%d/%m/%Y"))
        print("Vacina aplicada: ", self.vaccine.type)
        print(f"Paciente: {self.citizen.nome} || Sus: {self.citizen.sus}") #cidadao
        print(f"Enfermeiro: {self.nurse.name} || Cip: {self.nurse.cip}") #enfermeiro
        print("----------------\n")
        
