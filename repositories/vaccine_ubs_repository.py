from models import *
from repositories import *

from database.conexao import connection

class Vaccine_ubs_repository():
    def __init__(self):
        self.vaccine_repo = Vaccine_repository()
        self.ubs_repo = Ubs_repository()

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
    
    def build_object_vaccine_ubs(self, rows):
        ubs_vaccines = []

        for row in rows:

            ubs_vac = Vaccine_ubs(
                vaccine = self.vaccine_repo.search_per_id(row["id_vacina"]),
                ubs = self.ubs_repo.search_per_id(row["id_ubs"]),
                dose = row["dose"],
                lote = row["num_lote"],
                available_quan = row["quantidade_disponivel"],
                validity = row["validade"],
            )

            ubs_vac.id_vaccine_ubs = row["id_vacina_ubs"]

            ubs_vaccines.append(ubs_vac)

        return ubs_vaccines