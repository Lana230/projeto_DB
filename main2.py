from models import *
from repositories import *
from menus.menu_appointment import Menu_appoi_doctor
from datetime import date

address1 = Address("55395-000","Pernambuco", "Jupi", "Rural", "Povado de Santa Rita", 234)

ubs1 = Ubs("PSF JOAO MONTEIRO", address1)

person1 = Pessoa("Livia", "solteira", ubs1)

email1 = Email("livinhaCarvalho@gmail.com", Tipo.MEDICO, person1, ubs1)

cell = Telefone(988657483, Tipo.MEDICO, person1, ubs1)

doc1 = Documento(TipoDocumento.CPF, "876.345.321-65")

person1.adicionar_email(email1)
person1.adicionar_telefone(cell)
person1.adicionar_documentos(doc1)

doctor1 = Medico()

menu_consulta = Menu_appoi_doctor()