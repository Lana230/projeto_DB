from .vaccine import Vaccine
from .grupo_vulneravel import Grupo_vulneravel

from database.conexao import connection
con = connection()
cursor = con.cursor()

class Focus_priority:
    def __init__(self, vaccine: Vaccine, type_vuln_group: Grupo_vulneravel, ocupation):
        self.id_focus_pririty = None
        self.vaccine = vaccine
        self.type_vuln_group = type_vuln_group
        self.ocupation = ocupation

    def save_focus_priority_db(self, id_vaccine):
        cursor.execute(
            "INSERT INTO foco_prioridade (id_vacina, grupo_vulneravel, ocupacao) VALUES (?, ?, ?)",
            (id_vaccine, self.grupo_vulneravel.value, self.ocupacao)
        )