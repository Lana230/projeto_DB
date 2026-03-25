from models import *
from repositories import *
from enum import Enum

class Vaccine_ubs:
    def __init__(self, vaccine: Vaccine, ubs: Ubs, dose, lote, available_quan, validity):
        self.id_vaccine_ubs = None
        self.vaccine = vaccine
        self.ubs = ubs
        self.dose =  dose
        self.lote = lote
        self.available_quan = available_quan
        self.validity = validity
        self.focus_priority = []

    def add_focus_priority(self, focus_priority: Focus_priority):
        self.focus_priority.append(focus_priority)
        
    def ver_priority(service_line: Fila_atendimento):
        vac_ubs_repo = Vaccine_ubs_repository()
        citizen_repo = CidadaoRepository()

        if service_line.tipo_atendimento != TipoAtendimento.VACINA:
            raise ValueError("A linha de atendimento deve ser do tipo vacina para verificar a prioridade")

        for scheduling in service_line.agendamentos:
            if not (scheduling.vaccine and scheduling.vaccine.id_vaccine):
                continue

            vac_ubs = vac_ubs_repo.search_per_vaccine_id(scheduling.vaccine.id_vaccine)

            if not (vac_ubs and vac_ubs.vunlerable_group):
                continue

            grupos_cidadao = citizen_repo.listar_grupos(scheduling.cidadao.num_sus)
            for group in vac_ubs.vunlerable_group:
                if group in grupos_cidadao:
                    scheduling.prioridade_calculada += group.peso_prioridade
                    scheduling.motivo_prioridade += f"Pertence ao grupo vulnerável: {group.nome_grupo}"
                
    def details_vaccine(self):
        print("Vacina: ", self.name)
        print("Dose: ", self.dose)
        print("Lote: ", self.lote)