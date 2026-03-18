from models import *

from database.conexao import connection

class Ubs_repository():  
    #SALVAR UBS NO BANCO DE DADOS
    def save_ubs_db(self, ubs: Ubs, address: Address):
        con = connection()
        cursor = con.cursor()
        
        try:
            cursor.execute(
                "INSERT INTO ubs (nome, id_endereco) VALUE (?, ?)",
                (ubs.name, address.id_address)
            )

            ubs.id_ubs = cursor.lastrowid
            con.commit()
        
        finally:
            con.close()

        return ubs
     
    #CONSULTAS DO BANCO DE DADOS
    def search_all():
        cursor.execute(
            "SELECT u.id_ubs, u.nome AS nome_ubs, e.rua, e.bairro, e.numero, e.cidade, e.estado, e.cep FROM ubs u INNER JOIN endereco e ON u.id_endereco = e.id_endereco"
        )
        
        return cursor.fetchall()
    
    def search_per_name(name):
        cursor.execute(
            "SELECT * FROM ubs WHERE nome = ?", (name,)
        )
        
        return cursor.fetchall()
    
    def search_all_citizens(self, ubs: Ubs):
        cursor.execute(
            "SELECT p.id_pessoa, p.nome, c.num_sus, c.data_nascimento, c.genero, c.naturalidade FROM pessoa p INNER JOIN cidadao c ON p.id_pessoa = p.id_pessoa WHERE p.id_ubs = ?", (ubs.id_ubs)
        )
        
        return cursor.fetchall()
    
    def search_all_doctors(self, ubs: Ubs):
        cursor.execute(
            "SELECT p.cpf_pessoa, p.nome, m.crm, m.especialidade FROM pessoa p INNER JOIN medico m ON p.cpf_pessoa = m.cpf_pessoa WHERE p.id_ubs = ?", (ubs.id_ubs)
        )
        
        return cursor.fetchall()
    
    def search_all_nurses(self, ubs: Ubs):
        cursor.execute(
            "SELECT p.cpf_pessoa, p.nome, e.cip FROM pessoa p INNER JOIN enfermeiro e ON p.cpf_pessoa = e.cpf_pessoa WHERE p.id_ubs = ?", (ubs.id_ubs)
        )
        
        return cursor.fetchall()

        