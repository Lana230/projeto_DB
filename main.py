from models import *
from repositories import *
from datetime import date

addr1 = Address("63041-050", "Ceara", "Juazeiro", "triangulo", "Clotilde Noroes Mota", 235)

ubs1 = Ubs("Triangulo", addr1)

ubs1.details_Ubs()

pessoa1 = Pessoa(12345678900, 'Alana', ubs1)

email1 = Email("alanaclara@gmail.com", Tipo.CIDADAO, 12345678900)
email2 = Email("alana.silva@gmail.com", Tipo.MEDICO, 12345678900)

pessoa1.adicionar_email(email1)
pessoa1.adicionar_email(email2)

telefone1 = Telefone(11999999999, Tipo.CIDADAO, 12345678900)
telefone2 = Telefone(88922222222, Tipo.MEDICO, 12345678900)

pessoa1.adicionar_telefone(telefone1)
pessoa1.adicionar_telefone(telefone2)

pessoa1.exibir()

appointment1 = Appointment(pessoa1, None, ubs1, date.today(), "Consulta de rotina", "Paciente em bom estado de saúde")

exam1 = Exam(appointment1, "Hemograma Completo", Type_exam.EXAM_LAB, "Baixa", Status_exam.SCHEDULED)
exam1.add_data(date.today())
exam1.details_exam()

print(Type_exam.EXAM_CARD.value)

address_repo = Address_repository()
ubs_repo = Ubs_repository()

address_repo.save_address_db(addr1)

ubs_repo.save_ubs_db(ubs1)



