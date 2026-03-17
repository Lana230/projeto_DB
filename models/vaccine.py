from .cidadao import Cidadao
from .grupo_vulneravel import Grupo_vulneravel
from .focus_priority import Focus_priority
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

    def add_focus_priority(self, focus_priority: Focus_priority):
        self.focus_priority.append(focus_priority)

    def details_vaccine(self):
        print("Vacina: ", self.name)
        print("Dose: ", self.dose)
        print("Lote: ", self.lote)

    #SALVANDO VACINA NO BANCO DE DADOS
    def save_vaccine_db(self):
        cursor.execute(
            "INSERT INTO vacina(nome, previne, dose, lote, quant_disponivel, prioridade) VALUES (?, ?, ?, ?, ?, ?)",
            (self.name, self.prevents, self.dose, self.lote, self.available_quan, self.priority)
        )

        self.id_vaccine = cursor.lastrowid

        for fp in self.focus_priority:
            fp.save_focus_priority_db(self.id_vaccine)

    
            
