import unittest
from unittest.mock import Mock
from models.agendamento import Agendamento
from models.cidadao import Cidadao
from models.grupo_vulneravel import Grupo_vulneravel
from models.ubs import Ubs
from models.address import Address
from models.cidadao import Genero

class TestAgendamento(unittest.TestCase):

    def setUp(self):
        # Mock de objetos dependentes para evitar interações com o banco de dados ou outras lógicas complexas
        self.mock_ubs = Mock(spec=Ubs)
        self.mock_ubs.id_ubs = 1
        self.mock_ubs.name = "UBS Central"

        self.mock_address = Mock(spec=Address)
        self.mock_address.street = "Rua Principal"
        self.mock_address.number = "123"
        self.mock_address.neighborhood = "Centro"
        self.mock_address.city = "Cidade"
        self.mock_address.state = "Estado"
        self.mock_address.zip_code = "12345-678"

        self.mock_cidadao_base = Mock(spec=Cidadao)
        self.mock_cidadao_base.nome_pessoa = "Cidadao Teste"
        self.mock_cidadao_base.estado_civil = "Solteiro"
        self.mock_cidadao_base.ubs = self.mock_ubs
        self.mock_cidadao_base.num_sus = "123456789012345"
        self.mock_cidadao_base.data_nascimento = "1990-01-01"
        self.mock_cidadao_base.genero = Genero.FEMININO
        self.mock_cidadao_base.naturalidade = "Brasileira"
        self.mock_cidadao_base.ocupacao = "Estudante"
        self.mock_cidadao_base.address = self.mock_address
        self.mock_cidadao_base.grupos = []

    def test_calcular_prioridade_sem_grupos(self):
        # Cidadão sem grupos vulneráveis deve ter prioridade 0
        cidadao = self.mock_cidadao_base
        prioridade = Agendamento.calcular_prioridade(cidadao)
        self.assertEqual(prioridade, 0)

    def test_calcular_prioridade_com_um_grupo(self):
        # Cidadão com um grupo vulnerável
        mock_grupo1 = Mock(spec=Grupo_vulneravel)
        mock_grupo1.peso_prioridade = 5
        self.mock_cidadao_base.grupos = [mock_grupo1]
        
        cidadao = self.mock_cidadao_base
        prioridade = Agendamento.calcular_prioridade(cidadao)
        self.assertEqual(prioridade, 5)

    def test_calcular_prioridade_com_multiplos_grupos(self):
        # Cidadão com múltiplos grupos vulneráveis
        mock_grupo1 = Mock(spec=Grupo_vulneravel)
        mock_grupo1.peso_prioridade = 5
        mock_grupo2 = Mock(spec=Grupo_vulneravel)
        mock_grupo2.peso_prioridade = 10
        mock_grupo3 = Mock(spec=Grupo_vulneravel)
        mock_grupo3.peso_prioridade = 3
        self.mock_cidadao_base.grupos = [mock_grupo1, mock_grupo2, mock_grupo3]

        cidadao = self.mock_cidadao_base
        prioridade = Agendamento.calcular_prioridade(cidadao)
        self.assertEqual(prioridade, 18)

    def test_calcular_prioridade_com_grupos_vazios(self):
        # Cidadão com lista de grupos vazia
        self.mock_cidadao_base.grupos = []
        cidadao = self.mock_cidadao_base
        prioridade = Agendamento.calcular_prioridade(cidadao)
        self.assertEqual(prioridade, 0)

if __name__ == '__main__':
    unittest.main()
