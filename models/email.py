from models.ubs import Ubs
from enum import Enum

from typing import TYPE_CHECKING

if TYPE_CHECKING:
  from models.pessoa import Pessoa

class Tipo(Enum):
  CIDADAO = "Cidadão"
  MEDICO = "Médico"
  ENFERMEIRO = "Enfermeiro"
  UBS = "Ubs"

class Email:
  def __init__(self, email, pessoa: "Pessoa"=None, ubs: Ubs=None):
    
    self.id_email = None
    self.email = email
    self.pessoa = pessoa
    self.ubs = ubs
  
  @classmethod
  def criar_email(classe, email, tipo, pessoa: "Pessoa"=None, ubs: Ubs=None):
    if not isinstance(tipo, Tipo):
      try:
        tipo = Tipo(tipo)
      except ValueError:
        raise ValueError("Tipo inválido")
    
    if tipo == Tipo.Ubs:
      if ubs is None or pessoa is not None:
        raise ValueError("Email de UBS deve ter apenas ubs")
    else:
      if pessoa is None or ubs is not None:
        raise ValueError("Email de pessoa deve ter apenas pessoa")

    return classe(email, pessoa, ubs)