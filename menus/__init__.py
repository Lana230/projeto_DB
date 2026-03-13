#Centralizar todas as importações de todas as classes do projeto, para facilitar a importação em outros arquivos. Assim, ao invés de importar cada classe individualmente, podemos importar todas as classes de uma vez só, utilizando apenas "from models import *".

from models.address import Address
from models.anamnese import Anamnese
from models.appointment import Appointment
from models.cidadao import *
from models.email import *
from models.enfermeiro import Enfermeiro
from models.exam import *
from models.fila_atendimento import *
from models.grupo_vulneravel import Grupo_vulneravel
from models.medico import Medico
from models.pessoa import Pessoa
from models.telefone import Telefone
from models.ubs import Ubs
from models.vaccine_record import Vaccine_record
from models.vaccine import Vaccine
from models.medication import Medication