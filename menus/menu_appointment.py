from models import *
from repositories import *
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

def Menu_appoi_doctor(citizen: Agendamento, doctor: Medico, ubs: Ubs):
    '''Se este método recebe objetos do tipo cidadao, medico e ubs, então não precisa novamente se utilizar dos repositórios no método para gerar um objeto de cidadao, medico e ubs'''
     
    citizen_repo = CidadaoRepository()
    doctor_repo = MedicoRepository()
    ubs_repo = Ubs_repository()

    #Aqui é chamado os métodos dos repositórios que vai gerar um objeto
    doctor = doctor_repo.buscar_por_crm(doctor.crm)
    citizen = citizen_repo.buscar_por_sus(citizen.num_sus)
    ubs = ubs_repo.search_per_id(ubs.id_ubs)
    
    if not doctor:
        print("Medico nao encontrado.")
    if not citizen:
        print("Cidadao nao encontrado.")
    if not ubs:        
        print("UBS nao encontrada.") 
    
    if doctor and citizen and ubs:
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
                    elif op1 == 2:
                        sus_pacient = input("Digite o numero do SUS do paciente: ")
                        print(f"--- Consultas do paciente: {sus_pacient} ---")
                    elif op1 == 3:
                        entrada = input("Digite a data (dd/mm/aaaa): ")
                        data = datetime.strptime(entrada, "%d/%m/%Y").date()

                        print(f"--- Consultas realizadas no dia: {data}")

            elif op == 2:
                #Vai dá problema! O construtor espera valores, a não ser que você crie outro construtor que não passe nada
                #mas vai ter que ver se o python permite ter mais de um construtor na classe
                appointment = Appointment()

                print("---- NOVA CONSULTA ----")
                while True:
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

                        medication_repo = medication_repository()
                        # medication = medication_per_name()


            else:
                print("saindo...")
                break

def menu_appoi_citizen(citizen: Agendamento, doctor: Medico, ubs: Ubs):
    while True:
        print("--- Menu Consulta ---")
        print("1.Registro de consultas.")
        print("2. Sair")
        print("---------------------")

        op = input("Escolha: ")

        if op == 1:
            print("Todas as consultas desse paciente")
        elif op == 2:
            print("saindo...")
            break
