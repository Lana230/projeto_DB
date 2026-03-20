from models import Cidadao
from database.conexao import connection
from .pessoa_repository import PessoaRepository

'''nome_pessoa, estado_civil, ubs: Ubs, num_sus, data_nascimento, genero, naturalidade, ocupacao, address: Address'''

class CidadaoRepository():
    
    def salvar(self, cidadao: Cidadao):
        con = connection()
        cursor = con.cursor()
        
        if cidadao.id_pessoa is None:
            pessoa_repo = PessoaRepository()
            
            pessoa = pessoa_repo.salvar(cidadao)
            
            cidadao.id_pessoa = pessoa.id_pessoa
        
        cursor.execute("""
            INSERT INTO cidadao (
                num_sus, data_nascimento, genero, 
                naturalidade, ocupacao, id_endereco, 
                id_pessoa
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                cidadao.num_sus, 
                cidadao.data_nascimento,
                cidadao.genero,
                cidadao.naturalidade,
                cidadao.ocupacao,
                cidadao.address.id_address,
                cidadao.id_pessoa
            ))
        
        con.commit()
        con.close()
        
        return cidadao
        
        