from models import *

from database.conexao import connection

class Rec_vaccine_repository():
    def save_rec_vaccine_db(self, record_vaccine: Record_vaccine):
        con = connection()
        cursor =  con.cursor()

        try:
            cursor.execute(
                "INSERT INTO registro_vacina(num_sus, cip, id_ubs, data) VALUES (?, ?, ?, ?)",
                (record_vaccine.citizen.num_sus, record_vaccine.nurse.cip, record_vaccine.ubs.id_ubs, record_vaccine.data.isoformat())
            )

            record_vaccine.id_vaccine_record = cursor.lastrowid
            con.commit()
        
        except Exception as e:
            con.rollback() 
            print("Erro:", e)


        finally:
            con.close()