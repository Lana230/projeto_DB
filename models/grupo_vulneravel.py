from enum import Enum

class NomeGrupo(Enum):
    RECEM_NASCIDOS = "Recém-nascidos"
    CRIANCA = "Crianças"
    GESTANTE = "Gestantes"
    PUERPERA = "Puérperas"
    IDOSO = "Idosos"
    DOENCA_CRONICA = "Pessoas com doenças crônicas"
    DEFICIENCIA = "Pessoas com deficiência"
    SAUDE_MENTAl = "Pessoas com transtornos mentais"
    SITUACAO_DE_RUA = "Pessoas em situação de rua"
    INDIGENA = "População indígena"
    QUILOMBOLA = "População quilombola"
    PRIVADO_LIBERDADE = "População privada de liberdade"
    USUARIO_DROGAS = "Usuários de álcool e drogas"
    HIV_IST = "Pessoas com HIV/IST"
    ADOLESCENTE = "Adolescentes"
    VITIMA_VIOLENCIA = "Vítimas de violência"
    

class Grupo_vulneravel:
    
    def __init__(self, nome_grupo, peso_prioridade, descricao):
        
        self.id_grupo_vulneravel = None
        self.nome_grupo = nome_grupo if isinstance(nome_grupo, NomeGrupo) else NomeGrupo(nome_grupo)
        self.peso_prioridade = peso_prioridade
        self.descricao = descricao