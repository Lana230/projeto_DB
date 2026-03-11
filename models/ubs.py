from models.address import Address

class Ubs:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def details_Ubs(self):
        print("\n--- UBS ---")
        print(f"Nome: {self.name}\n")
        self.address.show_address()


        