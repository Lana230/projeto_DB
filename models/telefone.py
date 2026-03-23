from models.email import Tipo, Pessoa, Ubs

class Telefone:
  def __init__(self, num_telefone, pessoa: Pessoa, ubs: Ubs):
    
    self.id_telefone = None
    self.num_telefone = num_telefone
    self.pessoa = pessoa
    self.ubs = ubs

  @classmethod
  def criar_telefone(classe, num_telefone, tipo, pessoa: Pessoa, ubs: Ubs):
    if not isinstance(tipo, Tipo):
      try:
        tipo = Tipo(tipo)
      except ValueError:
        raise ValueError("Tipo inválido")
    
    if tipo == Tipo.UBS:
      if ubs is None or pessoa is not None:
        raise ValueError("Telefone de UBS deve ter apenas ubs")
      elif pessoa is None or ubs is not None:
        raise ValueError("Telefone de pessoa deve ter apenas pessoa")
    
    return classe(num_telefone, pessoa, ubs)