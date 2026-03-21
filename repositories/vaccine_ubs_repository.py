from models import *

from database.conexao import connection

class Vaccine_ubs_repository():
    #SALVANDO VACINA NO BANCO DE DADOS
    def save_vaccine_ubs_db(self, vaccine_ubs: Vaccine_ubs):
        con = connection()
        cursor = con.cursor()
        
        try:        
            cursor.execute(
                "INSERT INTO vacina_ubs(id_vaccine, id_ubs, dose, lote, quant_disponivel, prioridade) VALUES (?, ?, ?, ?, ?, ?)",
                (vaccine_ubs.vaccine.id_vaccine, vaccine_ubs.ubs.id_ubs, vaccine_ubs.dose, vaccine_ubs.lote, vaccine_ubs.available_quan, vaccine_ubs.priority)
            )

            vaccine_ubs.id_vaccine_ubs = cursor.lastrowid

            for fp in self.focus_priority:
                fp.save_focus_priority_db(cursor, vaccine_ubs.id_vaccine_ubs)
        
        except Exception as e:
            con.rollback() 
            print("Erro:", e)
        
        finally:
            con.close()

        return vaccine_ubs