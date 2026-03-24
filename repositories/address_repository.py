import sqlite3
from models import Address
from database.conexao import connection

class Address_repository():
    #SALVAR ENDERECO NO BANCO DE DADOS
    def save_address_db(self, address: Address):
        con = connection()
        cursor = con.cursor()

        try:
            cursor.execute(
                "INSERT INTO endereco (rua, bairro, numero, cidade, estado, cep) VALUES (?, ?, ?, ?, ?, ?)",
                (address.street, address.neigh, address.number, address.city, address.state, address.cep)
            )

            address.id_address = cursor.lastrowid
            con.commit()
        
        except Exception as e:
            con.rollback() 
            print("Erro:", e)

        finally:
            con.close()

        return address
    
    #CRIAR UMA LISTA DE ENDERECOS NO BANCO DE DADOS
    def build_object_address(self, rows):
        addresss = []

        for row in rows:
            if row is None:
                continue

            address = Address(
                cep = row["cep"],
                state = row["estado"],
                city = row["cidade"],
                neigh = row["bairro"],
                street = row["rua"],
                number = row["numero"],
            )

            address.id_address = row["id_endereco"]

            addresss.append(address)

        return addresss
    
    def search_per_ubs(self, id_ubs):
        con = connection() 
        con.row_factory = sqlite3.Row
        cursor = con.cursor()

        cursor.execute(
            "SELECT * FROM endereco WHERE id.ubs = ?", (id_ubs,)
        )

        row = cursor.fetchone()

        con.close()

        if row is None:
            return None
        
        return self.build_object_address([row])[0]
    
    def search_per_id(self, id_address):
        con = connection()
        con.row_factory = sqlite3.Row
        cursor = con.cursor()
        
        cursor.execute(
            "SELECT * FROM endereco WHERE id_endereco = ?", (id_address,)
        )
        
        row = cursor.fetchone()
        
        con.close()
        
        if row is None:
            return None
        
        return self.build_object_address([row])[0]