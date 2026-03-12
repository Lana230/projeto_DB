#Centralizar todas as importações de todas as classes do projeto, para facilitar a importação em outros arquivos. Assim, ao invés de importar cada classe individualmente, podemos importar todas as classes de uma vez só, utilizando apenas "from models import *".

from .address import Address
from .appointment import Appointment
from .cidadao import Cidadao
from .email import Email
from .telefone import Telefone
from .pessoa import Pessoa
from .exam import *
from .ubs import Ubs
from .vaccine_record import Vaccine_record
from .vaccine import Vaccine