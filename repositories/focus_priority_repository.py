from models import *

from database.conexao import connection

class Focus_priority_repository():
    def save_focus_priority(self, cursor, id_vaccine_ubs, focus_priority: Focus_priority):
        cursor.execute(
            "INSER INTO vacina_grupo(id_vacina_ubs, id_grupo) VALUES (?, ?)",
            (id_vaccine_ubs, focus_priority)
        )

        focus_priority.id_focus_pririty = cursor.lastrowid

        return focus_priority