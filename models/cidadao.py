from models.pessoa import Pessoa
from models.address import Address
from enum import Enum

class Genero(Enum):
  FEMININO = 'F'
  MASCULINO = 'M'

class Cidadao(Pessoa):
  def __init__(self, cpf, nome, id_ubs, sus, data_nascimento, genero, naturalidade, address):
    super().__init__(cpf, nome, id_ubs)
    self.sus = sus
    self.data_nascimento = data_nascimento
    self.genero = genero
    self.naturalidade = naturalidade
    self.address = address
    #deve adicionar listas para exames ligados ao cidadao?
    #suas consultas?
    #seus agendamentos?
    #e seus medicamentos?

  def exibir(self):
    super().exibir()
    print(f"SUS: {self.sus}")
    print(f"Data de Nascimento: {self.data_nascimento}")
    print(f"Gênero: {self.genero}")
    print(f"Naturalidade: {self.naturalidade}")
    self.address.show_address()