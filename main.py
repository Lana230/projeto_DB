from models.ubs import Ubs
from models.address import Address
from models.email import Email
from models.telefone import Telefone
from models.pessoa import Pessoa
from models.exam import Type_exam, Exam

addr1 = Address("63041-050", "Ceara", "Juazeiro", "triangulo", "Clotilde Noroes Mota", 235)

ubs1 = Ubs("Triangulo", addr1)

ubs1.details_Ubs()

pessoa = Pessoa(12345678900, 'Alana', 1)

email1 = Email("alanaclara@gmail.com", "cidadão", 12345678900)
email2 = Email("alana.silva@gmail.com", "médico", 12345678900)

pessoa.adicionar_email(email1)
pessoa.adicionar_email(email2)

telefone1 = Telefone(11999999999, "cidadão", 12345678900)
telefone2 = Telefone(88922222222, "médico", 12345678900)

pessoa.adicionar_telefone(telefone1)
pessoa.adicionar_telefone(telefone2)

pessoa.exibir()

print(Type_exam.EXAM_CARD.value)

