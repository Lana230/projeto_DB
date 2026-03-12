from models import Address, Ubs, Pessoa, Email, Telefone, Email, Appointment, Exam, Type_exam, Status_exam
from datetime import date

addr1 = Address("63041-050", "Ceara", "Juazeiro", "triangulo", "Clotilde Noroes Mota", 235)

ubs1 = Ubs("Triangulo", addr1)

ubs1.details_Ubs()

pessoa1 = Pessoa(12345678900, 'Alana', 1)

email1 = Email("alanaclara@gmail.com", "cidadão", 12345678900)
email2 = Email("alana.silva@gmail.com", "médico", 12345678900)

pessoa1.adicionar_email(email1)
pessoa1.adicionar_email(email2)

telefone1 = Telefone(11999999999, "cidadão", 12345678900)
telefone2 = Telefone(88922222222, "médico", 12345678900)

pessoa1.adicionar_telefone(telefone1)
pessoa1.adicionar_telefone(telefone2)

pessoa1.exibir()

appointment1 = Appointment(pessoa1, None, ubs1, date.today(), "Consulta de rotina", "Paciente em bom estado de saúde")

exam1 = Exam(appointment1, "Hemograma Completo", Type_exam.EXAM_LAB, "Baixa", Status_exam.SCHEDULED)
exam1.details_exam()

print(Type_exam.EXAM_CARD.value)

