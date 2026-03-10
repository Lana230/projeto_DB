class Address:
    def __init__(self, cep, state, city, neigh, street, number):
        self.cep = cep
        self.state = state
        self.city = city
        self.neigh = neigh
        self.street = street
        self.number = number
    
    def show_address(self):
        print("\n--- Endereço ---")
        print("CEP:", self.cep)
        print("Estado:", self.state)
        print("Cidade:", self.city)
        print("Bairro:", self.neigh)
        print("Rua:", self.street)
        print("Número:", self.number)
        print("----------------\n")

