from .ubs import Ubs
from .medication import Medication

from database.conexao import connection
con = connection()
cursor = con.cursor()

class Medication_ubs(Medication):
    def __init__(self, name_medication, category_med, ubs: Ubs, num_lote, available_quantity, validity):
        super.__init__(name_medication, category_med)
        self.id_medication_ubs = None
        self.ubs = ubs
        self.num_lote = num_lote
        self.available_quantity = available_quantity
        self.validity =  validity

    #SALVANDO MEDICACAO_UBS NO BANCO DE DADOS
    def save_medication_ubs_db(self):
        
        super().save_medication_db()

        cursor.execute(
            "INSERT INTO medicamento_ubs(id_medicamento, id_ubs, num_lote, quantidade_disponivel, validade) VALUES (?, ?, ?, ?, ?)",
            (self.id_medication, self.ubs.id_ubs, self.num_lote, self.available_quantity, self.validity)
        )
        
        self.id_medication_ubs = cursor.lastrowid