from models.pessoa import Pessoa
from models.address import Address

class Cidadao(Pessoa):
  def __init__(self, cpf, nome, id_ubs, sus, data_nascimento, genero, naturalidade):
    super().__init__(cpf, nome, id_ubs)
    self.sus = sus
    self.data_nascimento = data_nascimento
    self.genero = genero
    self.naturalidade = naturalidade

  def adicionar_endereco(self, id_endereco, rua, numero, bairro, cidade, estado):
    self.endereco = Address(id_endereco, rua, numero, bairro, cidade, estado)
