from models.pessoa import Pessoa
from enum import Enum

class Tipo(Enum):
  CIDADAO = "Cidadão"
  MEDICO = "Médico"
  ENFERMEIRO = "Enfermeiro"
  UBS = "Ubs"

class Email:
  def __init__(self, email, tipo, pessoa: Pessoa):
    self.email = email
    self.tipo = tipo
    self.pessoa = pessoa

    #alteração no tipo de valor esperado no atributo tipo
    #para médico, cidadão ou enfermeiro
    #para indicar a que tipo de pessoa pertence

  def adicionar_id(self, id_email):
    self.id_email = id_email