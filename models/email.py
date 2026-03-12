from enum import Enum

class Tipo(Enum):
  CIDADAO = "Cidadão"
  MEDICO = "Médico"
  ENFERMEIRO = "Enfermeiro"

class Email:
  def __init__(self, email, tipo, cpf_pessoa):
    self.email = email
    self.tipo = tipo
    self.cpf_pessoa = cpf_pessoa

    #alteração no tipo de valor esperado no atributo tipo
    #para médico, cidadão ou enfermeiro
    #para indicar a que tipo de pessoa pertence

  def adicionar_id_email(self, id_email):
    self.id_email = id_email