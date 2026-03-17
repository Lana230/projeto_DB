from models.pessoa import *
from models.address import Address
from enum import Enum

class Genero(Enum):
  FEMININO = 'F'
  MASCULINO = 'M'

class Cidadao(Pessoa):
  def __init__(self, nome_pessoa, estado_civil, ubs: Ubs, num_sus, data_nascimento, genero, naturalidade, ocupacao, address: Address):
    super().__init__(nome_pessoa, estado_civil, ubs)
    
    self.num_sus = num_sus
    self.data_nascimento = data_nascimento
    self.genero = genero
    self.naturalidade = naturalidade
    self.ocupacao = ocupacao
    self.address = address
    #deve adicionar listas para exames ligados ao cidadao? sim
    #suas consultas? sim
    #seus agendamentos? sim
    #e seus medicamentos? estaria vinculado as consultas na qual passaram os medicamentos

  def exibir(self):
    super().exibir()
    
    print(f"SUS: {self.num_sus}")
    print(f"Data de Nascimento: {self.data_nascimento}")
    print(f"Gênero: {self.genero}")
    print(f"Naturalidade: {self.naturalidade}")
    print(f"Ocupação: {self.ocupacao}")
    
    self.address.show_address()