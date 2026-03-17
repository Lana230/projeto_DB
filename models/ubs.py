from models.address import Address

from database.conexao import connection
con = connection()
cursor = con.cursor()

class Ubs:
    def __init__(self, name, address: Address):
        self.id_ubs = None
        self.name = name
        self.address = address

    def details_Ubs(self):
        print("\n--- UBS ---")
        print(f"Nome: {self.name}\n")
        self.address.show_address()

    #SALVAR UBS DENTRO DO BANCO DE DADOS
    def save_ubs_db(self):
        cursor.execute(
            "INSERT INTO ubs (nome, id_endereco) VALUE (?, ?)",
            (self.name, self.address.id_address)
        )

        self.id_ubs = cursor.lastrowid

    #JUNCAO DE UBS COM SEU ENDERECO

    #CONSULTAS DO BANCO DE DADOS
    def search_all():
        cursor.execute(
            "SELECT u.id_ubs, u.nome AS nome_ubs, e.rua, e.bairro, e.numero, e.cidade, e.estado, e.cep FROM ubs u INNER JOIN endereco e ON u.id_endereco = e.id_endereco"
        )
        
        return cursor.fetchall()
    
    def search_per_name(name):
        cursor.execute(
            "SELECT * FROM ubs WHERE nome = ?", (name)
        )
        
        return cursor.fetchall()
    
    def search_all_citizens(self):
        cursor.execute(
            "SELECT p.cpf_pessoa, p.nome, c.num_sus, c.data_nascimento, c.genero, c.naturalidade FROM pessoa p INNER JOIN cidadao c ON p.cpf_pessoa = c.cpf_pessoa WHERE p.id_ubs = ?", (self.id_ubs)
        )
        
        return cursor.fetchall()
    
    def search_all_doctors(self):
        cursor.execute(
            "SELECT p.cpf_pessoa, p.nome, m.crm, m.especialidade FROM pessoa p INNER JOIN medico m ON p.cpf_pessoa = m.cpf_pessoa WHERE p.id_ubs = ?", (self.id_ubs)
        )
        
        return cursor.fetchall()
    
    def search_all_nurses(self):
        cursor.execute(
            "SELECT p.cpf_pessoa, p.nome, e.cip FROM pessoa p INNER JOIN enfermeiro e ON p.cpf_pessoa = e.cpf_pessoa WHERE p.id_ubs = ?", (self.id_ubs)
        )
        
        return cursor.fetchall()