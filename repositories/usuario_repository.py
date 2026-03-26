import sqlite3
from database.conexao import connection

from models.usuario import Usuario, TipoUsuario

from .ubs_repository import Ubs_repository

class Usuario_repository():
    
    def __init__(self):
        self.ubs_repo = Ubs_repository()
    
    def salvar(self, usuario: Usuario):
        con = connection()
        cursor = con.cursor()
        
        cursor.execute("""
            INSERT INTO usuario (
                id_ubs, nome_usuario, email,
                senha, tipo
            ) VALUES (?, ?, ?, ?, ?)
            """, (
                usuario.ubs.id_ubs,
                usuario.nome_usuario,
                usuario.email,
                usuario.senha,
                usuario.tipo.value
            ))
        
        usuario.id_usuario = cursor.lastrowid
        
        con.commit()
        con.close()
        
        return usuario
    
    def buscar_por_login(self, email):
        con = connection()
        con.row_factory = sqlite3.Row
        cursor = con.cursor()
        
        cursor.execute("SELECT * FROM usuario WHERE email = ?", (email,))
        
        row = cursor.fetchone()
        
        con.close()
        
        ubs = self.ubs_repo.search_per_id(row["id_ubs"])
        
        usuario = Usuario(
            ubs=ubs,
            nome_usuario=row["nome_usuario"],
            email=row["email"],
            senha=row["senha"],
            tipo=TipoUsuario(row["tipo"])
        )
        
        return usuario