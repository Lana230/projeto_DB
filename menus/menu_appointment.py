from models.ubs import Ubs
from models.medico import Medico
from models.cidadao import Cidadao
from models.appointment import Appointment
from datetime import datetime

from database.conexao import conection
con = conection()
cursor = con.cursor()

def menu_appoi_doctor(appoi: Appointment, citizen: Cidadao, doctor: Medico, ubs: Ubs): 
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
                    appoi.search_all()
                elif op1 == 2:
                    sus_pacient = input("Digite o numero do SUS do paciente: ")
                    print(f"--- Consultas do paciente: {sus_pacient} ---")
                    appoi.search_per_citizen(sus_pacient)
                elif op1 == 3:
                    entrada = input("Digite a data (dd/mm/aaaa): ")
                    data = datetime.strptime(entrada, "%d/%m/%Y").date()

                    print(f"--- Consultas realizadas no dia: {data}")
                    appoi.search_per_data(data)

        elif op == 2:
            print("Preencher nova consulta:")
            
        else:
            print("saindo...")
            break

def menu_appoi_citizen(citizen: Cidadao, doctor: Medico, ubs: Ubs):
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
