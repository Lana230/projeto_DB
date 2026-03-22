from models.email import Tipo, Pessoa, Ubs

class Telefone:
  def __init__(self, num_telefone, tipo, pessoa: Pessoa, ubs: Ubs):
    
    self.id_telefone = None
    self.num_telefone = num_telefone
    self.tipo = tipo if isinstance(tipo, Tipo) else Tipo(tipo)
    self.pessoa = pessoa
    self.ubs = ubs

    #alteração no tipo de valor esperado no atributo tipo
    #para médico, cidadão ou enfermeiro
    #para indicar a que tipo de pessoa pertence