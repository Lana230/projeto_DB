import sqlite3
from database.conexao import connection

from models.vaccine import Vaccine

class Vaccine_repository():
    def save(self, vaccine: Vaccine):
        con = connection()
        cursor = con.cursor()

        try:
            cursor.execute(
                "INSERT INTO vacina(tipo, fabricante, previne) VALUES (?, ?, ?)",
                (vaccine.type_vaccine, vaccine.vaccine_manufacturer, vaccine.prevents)
            )

            vaccine.id_vaccine = cursor.lastrowid
            con.commit()
        
        except Exception as e:
            con.rollback() 
            print("Erro:", e)

        finally:
            con.close()

        return vaccine
    
    def build_object(self, rows):
        vaccines = []

        for row in rows:
            if row is None:
                continue

            vaccine = Vaccine(
                type_vaccine = row["tipo"],
                vaccine_manufacturer = row["frabricante"],
                prevents = row["previne"],
            )

            vaccine.id_vaccine = row["id_vacina"]

            vaccines.append(vaccine)
        
        return vaccines
    
    def search_per_id(self, id_vaccine):
        con = connection()
        con.row_factory = sqlite3.Row
        cursor = con.cursor()

        cursor.execute(
            "SELECT * FROM vacina WHERE id_vacina = ?", 
            (id_vaccine,)
        )

        row = cursor.fetchone()

        con.close()

        if row is None:
            return None
        
        return self.build_object([row])[0]