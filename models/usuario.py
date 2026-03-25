from models.ubs import Ubs
from enum import Enum

class TipoUsuario(Enum):
    ADMINISTRADOR = "Administrador"
    CIDADAO = "Cidadão"
    ENFERMEIRO = "Enfermeiro"
    MEDICO = "Médico"

class Usuario:
    
    def __init__(self, ubs: Ubs, nome_usuario, email, senha, tipo):
        
        self.id_usuario = None
        self.ubs = ubs
        self.nome_usuario = nome_usuario
        self.email = email
        self.senha = senha
        self.tipo = tipo if isinstance(tipo, TipoUsuario) else TipoUsuario(tipo)
    
    def exibir(self):
        print(f"Nome do usuário: {self.nome_usuario}")
        print(f"Email: {self.email}")
        print(f"Tipo de usuário: {self.tipo.value}")