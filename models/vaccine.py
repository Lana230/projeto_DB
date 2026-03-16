from .cidadao import Cidadao
from .grupo_vulneravel import Grupo_vulneravel
from enum import Enum

from database.conexao import connection
con = connection()
cursor = con.cursor()

class priority(Enum):
    VERY_HIGH = "Muito Alta"
    HIGH = "Alta"
    MEDIUM = "Media"
    LOW = "Baixa"

class Vaccine:
    def __init__(self, name, prevents, dose, lote, available_quan):
        self.id_vaccine = None
        self.name = name
        self.priority = None
        self.dose =  dose
        self.lote = lote
        self.prevents = prevents
        self.available_quan = available_quan
        self.focus_priority = []
    
    #def ver_priority(citizen: Cidadao):
        #se o cidadao for idoso, doencas cronicas, profissional da saude, Imunossuprimidos(Muito alta)
        #se o cidadao for profissionais da seguranca, professores, gestantes ou perpura e pcd(Alta)
        #se o cidadao

    #def add_focus_priority(type_vuln_group: Grupo_vulneravel, ocupation):
        #self.add_focus_priority.append(type_vuln_group)
        #self.add_focus_priority(ocupation)

    def add_id(self, id_vaccine):
        self.id_vaccine = id_vaccine

    def details_vaccine(self):
        print("Vacina: ", self.name)
        print("Dose: ", self.dose)
        print("Lote: ", self.lote)

