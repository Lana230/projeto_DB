class Anamnese:
    def __init__(self, sus, id_consulta, peso, altura, pressao_arterial):
        self.sus = sus
        self.id_consulta = id_consulta
        self.peso = peso
        self.altura = altura
        self.pressao_arterial = pressao_arterial
        
    def adicionar_id(self, id_anamnese):
        self.id_anamnese = id_anamnese