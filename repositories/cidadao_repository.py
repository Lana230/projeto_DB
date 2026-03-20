import sqlite3
from models import Cidadao, Ubs
from database.conexao import connection
from .pessoa_repository import PessoaRepository
from .ubs_repository import Ubs_repository
from .address_repository import Address_repository

class CidadaoRepository():
    
    def __init__(self):
        self.pessoa_repo = PessoaRepository()
        self.ubs_repo = Ubs_repository()
        self.address_repo = Address_repository()
    
    def salvar(self, cidadao: Cidadao):
        con = connection()
        cursor = con.cursor()
        
        if cidadao.id_pessoa is None:
            pessoa = self.pessoa_repo.salvar(cidadao)
            cidadao.id_pessoa = pessoa.id_pessoa
        
        cursor.execute("""
            INSERT INTO cidadao (
                num_sus, data_nascimento, genero, 
                naturalidade, ocupacao, id_endereco, 
                id_pessoaz
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
        
    def costruir_objeto(self, rows):
        cidadaos = []
        
        for row in rows:
            if row is None:
                continue
            
            ubs = self.ubs_repo.search_per_id(row["id_ubs"])
            #address = self.address_repo.search_per_id(row["id_endereco"])
            
            cidadao = Cidadao(
                nome_pessoa=row["nome_pessoa"],
                estado_civil=row["estado_civil"],
                ubs=ubs,
                num_sus=row["num_sus"],
                data_nascimento=row["data_nascimento"],
                genero=row["genero"],
                naturaliddade=row["naturalidade"],
                ocupacao=row["ocupacao"],
                address=None #chamar o repositorio de endereco
            )
            
            cidadao.id_pessoa = row["id_pessoa"]
            
            cidadaos.append(cidadao)
        
        return cidadaos
    
    def listar_todos_por_ubs(self, ubs: Ubs):
        con = connection()
        con.row_factory = sqlite3.Row
        cursor = con.cursor()

        cursor.execute("""
            SELECT 
                p.id_pessoa, p.nome_pessoa, p.id_ubs, p.estado_civil, 
                c.num_sus, c.data_nascimento, c.genero, 
                c.naturalidade, c.ocupacao, c.id_endereco 
                FROM pessoa p INNER JOIN cidadao c ON p.id_pessoa = c.id_pessoa WHERE p.id_ubs = ?
            """, (ubs.id_ubs,)
        )
        
        rows =  cursor.fetchall()
        
        con.close()
        
        return self.costruir_objeto(rows)