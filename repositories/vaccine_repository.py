from models import *

from database.conexao import connection

class Vaccine_repository():
    def save_vaccine_db(self, vaccine: Vaccine):
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