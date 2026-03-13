#Centralizar todas as importações de todas as classes do projeto, para facilitar a importação em outros arquivos. Assim, ao invés de importar cada classe individualmente, podemos importar todas as classes de uma vez só, utilizando apenas "from models import *".

from .address import Address
from .anamnese import Anamnese
from .appointment import Appointment
from .cidadao import *
from .email import *
from .enfermeiro import Enfermeiro
from .exam import *
from .fila_atendimento import *
from .grupo_vulneravel import Grupo_vulneravel
from .medico import Medico
from .pessoa import Pessoa
from .telefone import Telefone
from .ubs import Ubs
from .vaccine_record import Vaccine_record
from .vaccine import Vaccine
from .medication import Medication
from .hypothesis import Hypothesis