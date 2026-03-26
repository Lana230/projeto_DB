import sqlite3

from models import *
from repositories import *

from database.conexao import connection

class Vaccine_ubs_repository():
    def __init__(self):
        self.vaccine_repo = Vaccine_repository()
        self.ubs_repo = Ubs_repository()

    #SALVANDO VACINA NO BANCO DE DADOS
    def save(self, vaccine_ubs: Vaccine_ubs):
        con = connection()
        cursor = con.cursor()
        
        try:
            if vaccine_ubs.vaccine and vaccine_ubs.vaccine.id_vaccine is None:
                vaccine_ubs = self.vaccine_repo.save(vaccine_ubs.vaccine)

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
    
    def build_object(self, rows):
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
    
    def search_all(self):
        con = connection()
        cursor = con.cursor()

        try:
            cursor.execute("SELECT * FROM vacina_ubs")
            rows = cursor.fetchall()
            return self.build_object(rows)

        except Exception as e:
            print("Erro:", e)
        
        finally:
            con.close()

    def search_per_id_vaccine(self, id_vaccine):
        con = connection()
        cursor = con.cursor()

        try:
            cursor.execute("SELECT * FROM vacina_ubs WHERE id_vaccine = ?", (id_vaccine,))
            rows = cursor.fetchall()
            return self.build_object(rows)

        except Exception as e:
            print("Erro:", e)
        
        finally:
            con.close()

    def search_per_ubs(self, id_ubs):
        con = connection()
        con.row_factory = sqlite3.Row
        cursor = con.cursor()

        cursor.execute(
            "SELECT * FROM vacina_ubs WHERE id_ubs = ?",
            (id_ubs,)
        )
        rows = cursor.fetchall()

        con.close()

        if rows is None:
            return None

        return self.build_object(rows) 
    
    def update_available_quan(self, vaccine_ubs: Vaccine_ubs):
        con = connection()
        cursor = con.cursor()

        try:
            cursor.execute(
                "UPDATE vacina_ubs SET quant_disponivel = ? WHERE id_vacina_ubs = ?",
                (vaccine_ubs.available_quan, vaccine_ubs.id_vaccine_ubs)
            )
            con.commit()

        except Exception as e:
            con.rollback()
            print("Erro:", e)
        
        finally:
            con.close()