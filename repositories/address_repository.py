from models import *

from database.conexao import connection

class Address_repository():
    #SALVAR ENDERECO NO BANCO DE DADOS
    def save_address_db(self, address: Address):
        con = connection()
        cursor = con.cursor()

        try:
            cursor.execute(
                "INSERT INTO endereco (cep, estado, cidade, bairro, rua, numero) VALUES (?, ?, ?, ?, ?, ?)",
                (address.cep, address.state, address.city, address.neigh, address.street, address.number)
            )

            address.id_address = cursor.lastrowid
            con.commit()
        
        finally:
            con.close()

        return address