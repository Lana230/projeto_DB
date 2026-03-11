from models.ubs import Ubs
from models.address import Address
from models.pessoa import Pessoa

addr1 = Address("63041-050", "Ceara", "Juazeiro", "triangulo", "Clotilde Noroes Mota", 235)

ubs1 = Ubs("Triangulo", addr1)

ubs1.details_Ubs()

pessoa = Pessoa(11665401389, 'Alana', 1)

pessoa.adicionar_email('alanaclara@gmail.com')
pessoa.adicionar_email('alana.silva@gmail.com')

pessoa.adicionar_telefone(11999999999)
pessoa.adicionar_telefone(88999132393)

pessoa.exibir()