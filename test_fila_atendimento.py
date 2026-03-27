import unittest
from unittest.mock import Mock
from models.fila_atendimento import Fila_atendimento, TipoAtendimento
from models.ubs import Ubs
from models.medico import Medico
from models.vaccine import Vaccine

class TestFilaAtendimento(unittest.TestCase):

    def setUp(self):
        self.mock_ubs = Mock(spec=Ubs)
        self.mock_ubs.id_ubs = 1
        self.mock_ubs.name = "UBS Teste"

        self.mock_medico = Mock(spec=Medico)
        self.mock_medico.crm = "CRM123"
        self.mock_medico.name = "Dr. Teste"

        self.mock_vacina = Mock(spec=Vaccine)
        self.mock_vacina.id_vaccine = 101
        self.mock_vacina.type_vaccine = "COVID-19"

    def test_criar_fila_consulta_valida(self):
        fila = Fila_atendimento.criar_fila(
            ubs=self.mock_ubs,
            tipo_atendimento=TipoAtendimento.CONSULTA,
            data_fila="2024-03-28",
            quantidade_maxima=10,
            medico=self.mock_medico
        )
        self.assertIsInstance(fila, Fila_atendimento)
        self.assertEqual(fila.tipo_atendimento, TipoAtendimento.CONSULTA)
        self.assertEqual(fila.medico, self.mock_medico)
        self.assertIsNone(fila.vacina)

    def test_criar_fila_vacina_valida(self):
        fila = Fila_atendimento.criar_fila(
            ubs=self.mock_ubs,
            tipo_atendimento=TipoAtendimento.VACINA,
            data_fila="2024-03-28",
            quantidade_maxima=20,
            vacina=self.mock_vacina
        )
        self.assertIsInstance(fila, Fila_atendimento)
        self.assertEqual(fila.tipo_atendimento, TipoAtendimento.VACINA)
        self.assertEqual(fila.vacina, self.mock_vacina)
        self.assertIsNone(fila.medico)

    def test_criar_fila_consulta_com_vacina_invalida(self):
        with self.assertRaises(ValueError) as cm:
            Fila_atendimento.criar_fila(
                ubs=self.mock_ubs,
                tipo_atendimento=TipoAtendimento.CONSULTA,
                data_fila="2024-03-28",
                quantidade_maxima=10,
                medico=self.mock_medico,
                vacina=self.mock_vacina
            )
        self.assertEqual(str(cm.exception), "Fila de consulta deve ter apenas médico")

    def test_criar_fila_vacina_com_medico_invalida(self):
        with self.assertRaises(ValueError) as cm:
            Fila_atendimento.criar_fila(
                ubs=self.mock_ubs,
                tipo_atendimento=TipoAtendimento.VACINA,
                data_fila="2024-03-28",
                quantidade_maxima=20,
                medico=self.mock_medico,
                vacina=self.mock_vacina
            )
        self.assertEqual(str(cm.exception), "Fila de vacinação deve ter apenas vacina")

    def test_criar_fila_quantidade_maxima_invalida(self):
        with self.assertRaises(ValueError) as cm:
            Fila_atendimento.criar_fila(
                ubs=self.mock_ubs,
                tipo_atendimento=TipoAtendimento.CONSULTA,
                data_fila="2024-03-28",
                quantidade_maxima=0,
                medico=self.mock_medico
            )
        self.assertEqual(str(cm.exception), "Quantidade máxima deve ser maior que zero")

    def test_criar_fila_ubs_nula(self):
        with self.assertRaises(ValueError) as cm:
            Fila_atendimento.criar_fila(
                ubs=None,
                tipo_atendimento=TipoAtendimento.CONSULTA,
                data_fila="2024-03-28",
                quantidade_maxima=10,
                medico=self.mock_medico
            )
        self.assertEqual(str(cm.exception), "UBS é obrigatória")

    def test_adicionar_agendamento(self):
        fila = Fila_atendimento.criar_fila(
            ubs=self.mock_ubs,
            tipo_atendimento=TipoAtendimento.CONSULTA,
            data_fila="2024-03-28",
            quantidade_maxima=10,
            medico=self.mock_medico
        )
        mock_agendamento = Mock()
        fila.adicionar_agendamento(mock_agendamento)
        self.assertIn(mock_agendamento, fila.agendamentos)

if __name__ == '__main__':
    unittest.main()
