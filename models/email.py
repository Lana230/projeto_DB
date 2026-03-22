from models.pessoa import Pessoa
from models.ubs import Ubs
from enum import Enum

class Tipo(Enum):
  CIDADAO = "Cidadão"
  MEDICO = "Médico"
  ENFERMEIRO = "Enfermeiro"
  UBS = "Ubs"

class Email:
  def __init__(self, email, tipo, pessoa: Pessoa, ubs: Ubs):
    
    self.id_email = None
    self.email = email
    self.tipo = tipo if isinstance(tipo, Tipo) else Tipo(tipo)
    self.pessoa = pessoa
    self.ubs = ubs

    #alteração no tipo de valor esperado no atributo tipo
    #para médico, cidadão ou enfermeiro
    #para indicar a que tipo de pessoa pertence