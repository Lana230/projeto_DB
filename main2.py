from models.address import Address
from models.ubs import Ubs
from models.medico import Medico
from models.email import Email, Tipo
from models.telefone import Telefone
from models.documento import Documento, TipoDocumento

from repositories.address_repository import Address_repository
from repositories.ubs_repository import Ubs_repository
from repositories.medico_repository import MedicoRepository

from menus.menu_appointment import Menu_appoi_doctor
from datetime import date

address1 = Address("55395-000","Pernambuco", "Jupi", "Rural", "Povado de Santa Rita", "234")

ubs1 = Ubs("PSF JOAO MONTEIRO", address1)

doctor1 = Medico("Livia", "Solteira", ubs1, "1021-PE", "Oftomologista")

email1 = Email("livinhaCarvalho@gmail.com", Tipo.MEDICO, doctor1, ubs1)

cell = Telefone("988657483", Tipo.MEDICO, doctor1, ubs1)

doc1 = Documento(TipoDocumento.CPF, "876.345.321-65")

doctor1.adicionar_email("livinhaCarvalho@gmail.com")
doctor1.adicionar_telefone("988657483")
doctor1.adicionar_documento(doc1)

#Só vai dá certo após resolver o fluxo circular entre appointment e exam

address_repo = Address_repository()
address1 = address_repo.save(address1)

ubs_repo = Ubs_repository()
ubs1 = ubs_repo.save(ubs1)

#faltará chamar o repositorio de email, telefone e documento

doctor_repo = MedicoRepository()
doctor1 = doctor_repo.salvar(doctor1)

#Não está sendo passado os parâmetros definidos no método
#menu_consulta = Menu_appoi_doctor()