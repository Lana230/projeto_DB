from models import * 
from enum import Enum

from database.conexao import connection
con = connection()
cursor = con.cursor()

class priority(Enum):
    VERY_HIGH = "Muito Alta"
    HIGH = "Alta"
    MEDIUM = "Media"
    LOW = "Baixa"

class Vaccine_ubs:
    def __init__(self, vaccine: Vaccine, ubs: Ubs, dose, lote, available_quan):
        self.id_vaccine_ubs = None
        self.vaccine = vaccine
        self.ubs = ubs
        self.priority = None
        self.dose =  dose
        self.lote = lote
        self.available_quan = available_quan
        self.focus_priority = []
    
    #def ver_priority(citizen: Cidadao):
        #se o cidadao for idoso, doencas cronicas, profissional da saude, Imunossuprimidos(Muito alta)
        #se o cidadao for profissionais da seguranca, professores, gestantes ou perpura e pcd(Alta)
        #se o cidadao

    def add_focus_priority(self, focus_priority: Focus_priority):
        self.focus_priority.append(focus_priority)

    def details_vaccine(self):
        print("Vacina: ", self.name)
        print("Dose: ", self.dose)
        print("Lote: ", self.lote)

   

    
            
