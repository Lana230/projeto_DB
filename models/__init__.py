#Centralizar todas as importações de todas as classes do projeto, para facilitar a importação em outros arquivos. Assim, ao invés de importar cada classe individualmente, podemos importar todas as classes de uma vez só, utilizando apenas "from models import *".

from .address import Address
from .agendamento import Agendamento, StatusAgendamento
from .anamnese import Anamnese
from .appointment import Appointment
from .cidadao import Agendamento, Genero
from .dependente import Dependente
from .documento import Documento, TipoDocumento
from .email import Email, Tipo
from .enfermeiro import Enfermeiro
from .exam import Exam, Exam_Type, Status_exam, Type_degree
from .fila_atendimento import Fila_atendimento, TipoAtendimento
from .focus_priority import Focus_priority
from .grupo_vulneravel import Grupo_vulneravel, NomeGrupo
from .hypothesis import Hypothesis
from .medication_appoi import Medication_appoi, Via_medication
from .medication_ubs import Medication_ubs
from .medication import Medication
from .medico import Medico
from .pessoa import Pessoa
from .telefone import Telefone
from .ubs import Ubs
from .record_vaccine import Record_vaccine
from .vaccine_ubs import Vaccine_ubs, priority
from .vaccine import Vaccine