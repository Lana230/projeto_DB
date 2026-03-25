from .vaccine import Vaccine
from .grupo_vulneravel import Grupo_vulneravel

class Focus_priority:
    def __init__(self, vaccine: Vaccine, type_vuln_group: Grupo_vulneravel):
        self.id_focus_pririty = None
        self.vaccine = vaccine
        self.type_vuln_group = type_vuln_group