import sqlite3
from models import Ubs
from database.conexao import connection

class Ubs_repository():  
    #SALVAR UBS NO BANCO DE DADOS
    def save_ubs_db(self, ubs: Ubs):
        con = connection()
        cursor = con.cursor()
        
        try:
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
            u = Ubs(
                name=row["nome"],
                address=None #chamar o repositorio de address
            )
            
            u.id_ubs = row["id_ubs"]
            
            ubs.append(u)
        
        return ubs
     
    #CONSULTAS DO BANCO DE DADOS
    def search_all(self):
        con = connection()
        con.row_factory = sqlite3.Row
        cursor = con.cursor()

        cursor.execute(
            "SELECT u.id_ubs, u.nome, e.rua, e.bairro, e.numero, e.cidade, e.estado, e.cep FROM ubs u INNER JOIN endereco e ON u.id_endereco = e.id_endereco"
        )
        
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
    
    #NECESSARIO CORRRIGIR DEPOIS
    #retorna dados crus do banco de dados, um array com valores, em que cada valor vai está em um indice do array
    def search_all_citizens(self, ubs: Ubs):
        con = connection()
        cursor = con.cursor()

        cursor.execute(
            "SELECT p.id_pessoa, p.nome_pessoa, p.estado_civil, c.num_sus, c.data_nascimento, c.genero, c.naturalidade, c.ocupacao FROM pessoa p INNER JOIN cidadao c ON p.id_pessoa = c.id_pessoa WHERE p.id_ubs = ?", (ubs.id_ubs,)
        )
        
        citizens =  cursor.fetchall()
        
        con.close()
        
        return citizens
    
    def search_all_doctors(self, ubs: Ubs):
        con = connection()
        cursor = con.cursor()

        cursor.execute(
            "SELECT p.id_pessoa, p.nome_pessoa, p.estado_civil, m.crm, m.especialidade FROM pessoa p INNER JOIN medico m ON p.id_pessoa = m.id_pessoa WHERE p.id_ubs = ?", (ubs.id_ubs,)
        )
        
        doctors = cursor.fetchall()
        
        con.close()
        
        return doctors
    
    def search_all_nurses(self, ubs: Ubs):
        con = connection()
        cursor = con.cursor()

        cursor.execute(
            "SELECT p.id_pessoa, p.nome_pessoa, p.estado_civil, e.cip FROM pessoa p INNER JOIN enfermeiro e ON p.id_pessoa = e.id_pessoa WHERE p.id_ubs = ?", (ubs.id_ubs,)
        )
        
        nurses = cursor.fetchall()
        
        con.close()
        
        return nurses