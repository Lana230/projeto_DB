#importacion
#from citizen import Citizen(cidadao)
#from doctor import Doctor(medico)
from models.ubs import Ubs
from datetime import date

#class
class Appointment:
    def __init__(self, Citizen, Doctor, Ubs, data, reason, conclusion):
        self.citizen = Citizen
        self.doctor = Doctor
        self.Ubs = Ubs
        self.data = data
        self.reason = reason
        self.conclusion = conclusion

    def details_appoi(self):
        print("\n--- Consulta ---")
        print("UBS: ", self.Ubs.name)
        print(f"Paciente: {self.Citizen.name} || Numero do Sus: {self.Citizen.sus}") #adicione aqui a ligacao com cidadao
        print(f"Medico: {self.Doctor.name} || Numero do CRM: {self.Doctor.crm}") #adicione aqui a ligacao com medico
        print("Data: ", self.data.strtime("%d/%m/%Y"))
        print("Motivo: ", self.reason)
        print("Conclusao ", self.conclusion)
        print("----------------\n")