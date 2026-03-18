from .ubs import Ubs
from .medication import Medication

from database.conexao import connection
con = connection()
cursor = con.cursor()

class Medication_ubs():
    def __init__(self,  medication: Medication, ubs: Ubs, num_lote, available_quantity, validity):
        self.id_medication_ubs = None
        self.id_medication = medication.id_medication
        self.name_ubs_med = medication.name_medication
        self.cat_ubs_med = medication.category_med
        self.ubs = ubs
        self.num_lote = num_lote
        self.available_quantity = available_quantity
        self.validity =  validity

    #SALVANDO MEDICACAO_UBS NO BANCO DE DADOS
   