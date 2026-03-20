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