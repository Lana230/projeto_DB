from models import *
from repositories import *

from database.conexao import connection

class Focus_priority_repository():
    def __init__(self):
        self.vaccine_repo = Vaccine_repository()
        self.vunl_grup = Grupo_vulneravel_repository()

    def save(self, cursor, id_vaccine_ubs, focus_priority: Focus_priority):
        cursor.execute(
            "INSER INTO vacina_grupo(id_vacina_ubs, id_grupo) VALUES (?, ?)",
            (id_vaccine_ubs, focus_priority.type_vuln_group.id_grupo)
        )

        focus_priority.id_focus_pririty = cursor.lastrowid

        return focus_priority

    def build_object(self, rows):
        focus_prioritys = []

        for row in rows:

            focus_pri = Focus_priority(
                vaccine = self.vaccine_repo.search_per_id(row["id_vacina"]),
                type_vuln_group = self.vunl_grup.buscar_por_id(row["id_grupo"])
            )

            focus_prioritys.append(focus_pri)
        
        return focus_prioritys
    
    