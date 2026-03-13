class Vaccine:
    def __init__(self, name, prevents, dose, lote, available_quan):
        self.name = name
        self.dose =  dose
        self.lote = lote
        self.prevents = prevents
        self.available_quan = available_quan

    def details_vaccine(self):
        print("Vacina: ", self.name)
        print("Dose: ", self.dose)
        print("Lote: ", self.lote)

