import sqlite3
from database.conexao import connection

from models.ubs import Ubs

from .address_repository import Address_repository

class Ubs_repository():  
    def __init__(self):
        self.address_repo = Address_repository()

    #SALVAR UBS NO BANCO DE DADOS
    def save(self, ubs: Ubs):
        con = connection()
        cursor = con.cursor()
        
        try:
            if ubs.address and ubs.address.id_address is None:
                ubs.address = self.address_repo.save(ubs.address)

            cursor.execute(
                "INSERT INTO ubs (nome, id_endereco) VALUES (?, ?)",
                (ubs.name, ubs.address.id_address)
            )

            ubs.id_ubs = cursor.lastrowid
            con.commit()
        
        except Exception as e:
            con.rollback() 
            print("Erro:", e)

        finally:
            con.close()

        return ubs
    
    #CONSTRUTOR DE OBJETO
    #cria uma lista (array) de objetos do tipo ubs e retorna
    def build_object(self, rows):
        ubs = []
        
        for row in rows:
            if row is None:
                continue
            
            u = Ubs(
                name=row["nome"],
                address=self.address_repo.search_per_id(row["id_endereco"])
            )
            
            u.id_ubs = row["id_ubs"]
            
            ubs.append(u)
        
        return ubs
     
    #CONSULTAS DO BANCO DE DADOS
    def search_all(self):
        con = connection()
        con.row_factory = sqlite3.Row
        cursor = con.cursor()

        cursor.execute("""
            SELECT 
                u.id_ubs, u.nome, u.id_endereco 
                e.rua, e.bairro, e.numero, 
                e.cidade, e.estado, e.cep 
            FROM ubs u INNER JOIN endereco e ON u.id_endereco = e.id_endereco
        """)
        
        rows = cursor.fetchall()
        
        con.close()
        
        return self.build_object(rows)
    
    def search_per_id(self, id_ubs):
        con = connection()
        con.row_factory = sqlite3.Row
        cursor = con.cursor()
        
        cursor.execute("SELECT * FROM ubs WHERE id_ubs = ?", (id_ubs,))
        row = cursor.fetchone()
        
        con.close()
        
        if row is None:
            return None
        
        return self.build_object([row])[0]
    
    def search_per_name(self, name):
        con = connection()
        con.row_factory = sqlite3.Row
        cursor = con.cursor()

        cursor.execute(
            "SELECT * FROM ubs WHERE nome = ?", (name,)
        )
        
        row =  cursor.fetchone()
        
        con.close()
        
        if row is None:
            return None
        
        return self.build_object([row])[0]