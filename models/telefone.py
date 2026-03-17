from models.email import *

class Telefone:
  def __init__(self, num_telefone, tipo, pessoa: Pessoa, ubs: Ubs):
    
    self.num_telefone = num_telefone
    self.tipo = tipo
    self.pessoa = pessoa
    self.ubs = ubs

    #alteração no tipo de valor esperado no atributo tipo
    #para médico, cidadão ou enfermeiro
    #para indicar a que tipo de pessoa pertence

  def adicionar_id(self, id_telefone):
    self.id_telefone = id_telefone