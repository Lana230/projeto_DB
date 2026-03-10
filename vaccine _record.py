# from citizen import Citizen (cidadao)
#from nurse import Nurse (enfermeiro)
from vaccine import Vaccine

class Vaccine_record:
    def __init__(self, Citizen, Vaccine, Nurse, Ubs, data):
        self.citizen = Citizen #cidadao
        self.vaccine = Vaccine
        self.nurse = Nurse #enfermeiro
        self.ubs = Ubs
        self.data = data

    def record(self):
        print("UBS: ", self.ubs.name)
        print("Data: ", self.data.strtime("%d/%m/%Y"))
        print("Vacina aplicada: ", self.vaccine.type)
        print(f"Paciente: {self.citizen.name} || Sus: {self.citizen.sus}") #cidadao
        print(f"Enfermeiro: {self.nurse.name} || Cip: {self.nurse.cip}") #enfermeiro
        
