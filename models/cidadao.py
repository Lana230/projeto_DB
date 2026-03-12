from models.pessoa import Pessoa
from models.address import Address
from models.vaccine import Vaccine

class Cidadao(Pessoa):
  def __init__(self, cpf, nome, id_ubs, sus, data_nascimento, genero, naturalidade, address):
    super().__init__(cpf, nome, id_ubs)
    self.sus = sus
    self.data_nascimento = data_nascimento
    self.genero = genero
    self.naturalidade = naturalidade
    self.address = address

