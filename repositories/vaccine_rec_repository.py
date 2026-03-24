import sqlite3

from models import *
from repositories import *

from database.conexao import connection

class Rec_vaccine_repository():
    def __init__(self):
        self.ubs_vac_repo = Vaccine_ubs_repository()
        self.citizen_repo = CidadaoRepository()
        self.doctor_repo = MedicoRepository()
        self.nurse_repo = EnfermeiroRepository()
        self.ubs_repo = Ubs_repository()

    def save_rec_vaccine_db(self, record_vaccine: Record_vaccine, ubs_vaccine: Vaccine_ubs):
        con = connection()
        cursor =  con.cursor()

        try:
            cursor.execute(
                "INSERT INTO reg_vacina(num_sus, id_vacina_ubs, cip, id_ubs, data) VALUES (?, ?, ?, ?, ?)",
                (record_vaccine.citizen.num_sus, record_vaccine.vaccine_ubs.id_vaccine_ubs, record_vaccine.nurse.cip, record_vaccine.ubs.id_ubs, record_vaccine.data.isoformat())
            )

            record_vaccine.id_vaccine_record = cursor.lastrowid
            con.commit()
        
        except Exception as e:
            con.rollback() 
            print("Erro:", e)


        finally:
            con.close()

    def build_object_reg_vac(self, rows):
        rec_vaccines = []

        for row in rows:

            reg_vac = Record_vaccine(
                citizen = self.citizen_repo.buscar_por_sus(row["num_sus"]),
                vaccine_ubs = self.ubs_vac_repo.build_object_vaccine_ubs(row["id_vacina_ubs"]),
                nurse = self.nurse_repo, #adicionar procurar por id enfermeiro
                ubs = self.ubs_repo.search_per_id(row["id_ubs"]),
                data = row["id_data"],
            )

            reg_vac.id_vaccine_record = row["id_reg_vacina"]

            rec_vaccines.append(reg_vac)

        return rec_vaccines
    
    def show_rec_per_citizen(self, num_sus):
        con =  connection()
        con.row_factory = sqlite3.Row
        cursor = con.cursor()

        cursor.execute(
            "SELECT * FROM reg_vacina WHERE num_sus = ?",
            (num_sus,)
        )

        rows = cursor.fetchone()

        con.close()

        if rows is None:
            return None

        return self.build_object_reg_vac(rows) 
    
    