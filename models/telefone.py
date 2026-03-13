class Telefone:
  def __init__(self, num_telefone, tipo, cpf_pessoa):
    self.num_telefone = num_telefone
    self.tipo = tipo
    self.cpf_pessoa = cpf_pessoa

    #alteração no tipo de valor esperado no atributo tipo
    #para médico, cidadão ou enfermeiro
    #para indicar a que tipo de pessoa pertence

  def adicionar_id_telefone(self, id_telefone):
    self.id_telefone = id_telefone