from models.medico import Medico
from models.ubs import Ubs
from models.agendamento import Agendamento
from models.cidadao import Cidadao
from models.appointment import Appointment
from models.hypothesis import Hypothesis
from models.exam import Exam, Exam_Type, Status_exam, Type_degree
from models.medication_appoi import Medication_appoi, Via_medication

from repositories.agendamento_repository import AgendamentoRepository
from repositories.appointment_repository import AppointmentRepository
from repositories.cidadao_repository import CidadaoRepository
from repositories.ubs_repository import Ubs_repository
from repositories.medico_repository import MedicoRepository
from repositories.medication_repository import medication_repository
from repositories.medication_appoi_repository import Medication_appoi_repository

from datetime import datetime

def input_enum(enum_class):
        # monta dicionário (nome + valor)
        options = {e.name.lower(): e for e in enum_class}
        options.update({e.value.lower(): e for e in enum_class})

        while True:
            print("\nOpções:")
            for e in enum_class:
                print(f"- {e.name} ({e.value})")

            entrada = input("Escolha: ").strip().lower()

            if entrada in options:
                return options[entrada]
            else:
                print("Valor inválido, tenta de novo.")

class Class_menu_appointment:
    def __init__(self):
        self.agendamento_repo = AgendamentoRepository()
        self.appointment_repo = AppointmentRepository()
        self.cidadao_repo = CidadaoRepository()
        self.ubs_repo = Ubs_repository()
        self.doctor_repo = MedicoRepository()
        self.medication_repo = medication_repository()
        self.medication_appoi_repo = Medication_appoi_repository()

    def fill_out_appointment(self):
        while True:
            print("---- NOVA CONSULTA ----")
            num_sus = input("Digite o numero do SUS do paciente: ")
            citizen = self.cidadao_repo.buscar_por_sus(num_sus)
            if not citizen:
                print("Cidadao não encontrado no banco de dados. Tente novamente.")
                continue

            crm_doctor = input("Digite o CRM do médico: ")
            doctor = self.doctor_repo.buscar_por_crm(crm_doctor)
            if not doctor:
                print("Médico não encontrado no banco de dados. Tente novamente.")
                continue

            id_ubs = input("Digite o ID da UBS: ")
            ubs = self.ubs_repo.search_per_id(id_ubs)
            if not ubs:
                print("UBS não encontrada no banco de dados. Tente novamente.")
                continue   
    
            print("---- Dados da Ubs ----")
            ubs.details_Ubs()
            date = datetime.now()
            print(date)
            print("---- Dados do Medico Responsavel ----")
            doctor.exibir()
            print("---- Dados do Cidadao ----")
            citizen.exibir()
            print("---- Dados da Consulta ----")
            reason = input("Motivo: ")
            life_habites = input("Habitos de vida: ")

            appointment = Appointment(citizen, doctor, ubs, date, reason, life_habites)

            while True:
                continuar = input("Adicionar hipotese(s/n): ").lower()
                                
                if continuar not in ["s", "n"]:
                    print("Digite apenas 's' ou 'n'")
                    continue

                if continuar == "n":
                    break
                                    
                diseses = input("Nome da doenca: ")
                cid = input("CID: ")
                hypothesis_appoi = Hypothesis(appointment, diseses, cid)
                appointment.add_hypothesis(hypothesis_appoi)

            while True:
                continuar = input("Adicionar exame(s/n): ").lower()
                if continuar not in ["s", "n"]:
                    print("Digite apenas 's' ou 'n'")
                    continue

                if continuar == "n":
                    break

                name_exam = input("Exame: ")
                exam_type = input_enum(Exam_Type)
                status = input_enum(Status_exam)
                degree = input_enum(Type_degree)

                exam_appoi = Exam(appointment, name_exam, exam_type, status, degree)
                appointment.add_exam(exam_appoi)

            while True:
                continuar = input("Adicionar Medicamentos(s/n): ").lower()
                if continuar not in ["s", "n"]:
                    print("Digite apenas 's' ou 'n'")
                    continue

                if continuar == "n":
                    break
                                
                name_medication = input("Medicamento: ")
                medication = self.medication_repo.search_per_name(name_medication)
                if not medication:
                    print("Medicamento não encontrado no banco de dados. Tente novamente.")
                    continue
                                
                dosage = input("Dosagem: ")
                via = input_enum(Via_medication)
                frequency = input("Frequencia: ")
                duration = input("Duracao: ")
                                
                medication_appoi = Medication_appoi(medication, appointment, dosage,via, frequency, duration)
                appointment.add_medication(medication_appoi)
                    
            salvar = input("Salvar consulta? (s/n): ").lower()

            if salvar not in ["s", "n"]:
                print("Digite apenas 's' ou 'n'")
                continue

            if salvar == "s":
                self.appointment_repo.save(appointment)
                print("Consulta salva com sucesso!")
                return  
            else:
                print("Consulta não salva. Vamos preencher novamente...\n")
                break


    def Menu_appoi_doctor(self, doctor: Medico):
        
        doctor = self.doctor_repo.buscar_por_crm(self.doctor.crm)
        citizen = self.cidadao_repo.buscar_por_sus(self.cidadao.num_sus)
        ubs = self.ubs_repo.search_per_id(self.ubs.id_ubs)
        scheduling = self.scheduling_repo.buscar_por_id(self.scheduling.id_agendamento)
        
        if not (doctor and citizen and ubs and scheduling):
            print("Erro: Dados incompletos.")
            return

        while True:
            print("--- Menu Consulta ---")
            print("1.Registro de consultas.")
            print("2.Realizar nova consulta.")
            print("3. Sair")
            print("---------------------")

            op = input("Escolha: ")

            if op == '1':
                while True:
                    print("--- Consultas ---")
                    print("1. Todas as consultas.")
                    print("2. Consulta por cidadao.")
                    print("3. Consulta por data.")
                    print("4. Saindo.")
                        
                    op1 = input("Escolha: ")

                    if op1 == 1:
                        print("--- Todas as consultas ---")
                        appoi_all =self.appointment_repo.search_all(doctor_crm=doctor.crm, id_ubs=ubs.id_ubs)
                        for appoi in appoi_all:
                            print(f"Consulta ID: {appoi.id_appointment} | Data: {appoi.data} | Motivo: {appoi.reason}")
                            print("Hipoteses:")
                            appoi.show_hypothesis()
                            print("Exames:")
                            appoi.show_exams_names()
                            print("Medicamentos:")
                            appoi.show_medication()
                            print("\n---------------------\n")
                    elif op1 == 2:
                        sus_pacient = input("Digite o numero do SUS do paciente: ")
                        print(f"--- Consultas do paciente: {sus_pacient} ---")
                        appoi_citizen =self.appointment_repo.search_all(doctor_crm=doctor.crm, id_ubs=ubs.id_ubs, scheduling=Agendamento(cidadao=Cidadao(num_sus=sus_pacient)))
                        for appoi in appoi_citizen:
                            print(f"Consulta ID: {appoi.id_appointment} | Data: {appoi.data} | Motivo: {appoi.reason}")
                            print("Hipoteses:")
                            appoi.show_hypothesis()
                            print("Exames:")
                            appoi.show_exams_names()
                            print("Medicamentos:")
                            appoi.show_medication()
                            print("\n---------------------\n")
                    elif op1 == 3:
                        entrada = input("Digite a data (dd/mm/aaaa): ")
                        data = datetime.strptime(entrada, "%d/%m/%Y").date()
                        print(f"--- Consultas realizadas no dia: {data}")

                        appoi_data = self.appointment_repo.search_all(doctor_crm=doctor.crm, id_ubs=ubs.id_ubs, data=data)
                        for appoi in appoi_data:
                            print(f"Consulta ID: {appoi.id_appointment} | Data: {appoi.data} | Motivo: {appoi.reason}")
                            print("Hipoteses:")
                            appoi.show_hypothesis()
                            print("Exames:")
                            appoi.show_exams_names()
                            print("Medicamentos:")
                            appoi.show_medication()
                            print("\n---------------------\n")

            elif op == 2:

                while True:
                    self.fill_out_appointment()
                    nova_consulta = input("Deseja realizar outra consulta? (s/n): ").lower()
                    if nova_consulta not in ["s", "n"]: 
                        print("Digite apenas 's' ou 'n'")
                        continue
                    if nova_consulta == "n":
                        break
                               
            else:
                print("saindo...")
                break

    def menu_appoi_citizen(self, citizen: Cidadao):
        
        scheduling = self.scheduling_repo.buscar_por_id(self.scheduling.id_agendamento)
        citizen = self.cidadao_repo.buscar_por_sus(scheduling.cidadao.num_sus)
        ubs = self.ubs_repo.search_per_id(self.ubs.id_ubs)

        while True:
            print("--- Menu Consulta ---")
            print("1.Registro de consultas.")
            print("2. Sair")
            print("---------------------")

            op = input("Escolha: ")

            if op == 1:
                print("Todas as consultas desse paciente")
                appoi_citizen = self.appointment_repo.search_all(ubs.id_ubs,scheduling=Agendamento(cidadao=citizen))
                for appoi in appoi_citizen:
                    print(f"Consulta ID: {appoi.id_appointment} | Data: {appoi.data} | Motivo: {appoi.reason}")
                    print("Hipoteses:")
                    appoi.show_hypothesis()
                    print("Exames:")
                    appoi.show_exams_names()
                    print("Medicamentos:")
                    appoi.show_medication()
                    print("\n---------------------\n")
            elif op == 2:
                print("saindo...")
                break
