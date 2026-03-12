class Grupo_vulneravel:
    def __init__(self, nome_grupo, peso_prioridade):
        self.nome_grupo = nome_grupo
        self.peso_prioridade = peso_prioridade
        
    def adicionar_id(self, id_grupo_vulneravel):
        self.id_grupo_vulneravel = id_grupo_vulneravel