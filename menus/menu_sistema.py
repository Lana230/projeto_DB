import os

from models.usuario import Usuario, TipoUsuario
from models.pessoa import EstadoCivil
from models.email import Tipo
from models.cidadao import Cidadao, Genero
from models.enfermeiro import Enfermeiro
from models.medico import Medico
from models.address import Address

from repositories.cidadao_repository import CidadaoRepository
from repositories.enfermeiro_repository import EnfermeiroRepository
from repositories.medico_repository import MedicoRepository
from repositories.ubs_repository import Ubs_repository
from repositories.address_repository import Address_repository

def limpa_telinha():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except Exception as e:
        print("Erro:", e) 
        print("\033c", end = "")

def cadastrar_pessoa(tipo: Tipo):
    ubs_repo = Ubs_repository()
    
    limpa_telinha()
    
    nome_pessoa = input("Digite o nome da pessoa: ")
    
    while True:
        print(f"1 - {EstadoCivil.SOLTEIRO.value}")
        print(f"2 - {EstadoCivil.CASADO.value}")
        print(f"3 - {EstadoCivil.DIVORCIADO.value}")
        print(f"4 - {EstadoCivil.VIUVO.value}")
        print(f"5 - {EstadoCivil.UNIAO_ESTAVEL.value}")
        
        opcao = int(input("Escolha uma opcao: "))
        
        if opcao == 1:
            estado_civil = EstadoCivil.SOLTEIRO
            break
        elif opcao == 2:
            estado_civil = EstadoCivil.CASADO
            break
        elif opcao == 3:
            estado_civil = EstadoCivil.DIVORCIADO
            break
        elif opcao == 4:
            estado_civil = EstadoCivil.VIUVO
            break
        elif opcao == 5:
            estado_civil = EstadoCivil.UNIAO_ESTAVEL
            break
        else:
            print("Opção inválida!")
    
    while True:
        nome_ubs = input("Digite o nome da UBS na qual está vinculado: ")
        ubs = ubs_repo.search_per_name(nome_ubs)
        
        if ubs is None:
            print("Nome da UBS não existe!")
        else:
            break
    
    if tipo == Tipo.CIDADAO:
        cidadao_repo = CidadaoRepository()
        address_repo = Address_repository()
        
        num_sus = int(input("Digite o número do SUS: "))
        data_nascimento = input("Digite a sua data de nascimento (YYYY-MM-DD): ")
        
        while True:
            print(f"1 - {Genero.FEMININO.value}")
            print(f"2 - {Genero.MASCULINO.value}")
            
            opcao = int(input())
            
            if opcao == 1:
                genero = Genero.FEMININO
                break
            elif opcao == 2:
                genero = Genero.MASCULINO
                break
            else:
                print("Opção inválida!")
        
        naturalidade = input("Digite a sua naturalidade: ")
        ocupacao = input("Digite a sua ocupação: ")
                
        address = cadastrar_endereco()
        address = address_repo.save(address)
        
        cidadao = Cidadao(nome_pessoa, estado_civil, ubs, num_sus, data_nascimento, genero, naturalidade, ocupacao, address)
        
        cidadao = cidadao_repo.salvar(cidadao)
        return cidadao

    elif tipo == Tipo.ENFERMEIRO:
        enfermeiro_repo = EnfermeiroRepository()
        
        cip = input("Digite o seu CIP: ")
        
        enfermeiro = Enfermeiro(nome_pessoa, estado_civil, ubs, cip)
        
        enfermeiro = enfermeiro_repo.salvar(enfermeiro)
        return enfermeiro

    elif tipo == Tipo.MEDICO:
        medico_repo = MedicoRepository()
        
        crm = input("Digite o seu CRM: ")
        
        especialidade = input("Digite a sua especialidade: ")
        
        medico = Medico(nome_pessoa, estado_civil, ubs, crm, especialidade)
        
        medico = medico_repo.salvar(medico)
        return medico

def cadastrar_endereco():
    rua = input("Digite o nome da rua: ")
    bairro = input("Digite o nome do bairro: ")
    numero = input("Digite o número da sua residência: ")
    cidade = input("Digite a cidade onde vive: ")
    estado = input("Digite o estado onde vive: ")
    cep = input("Digite o seu CEP: ")
    
    address = Address(cep, estado, cidade, bairro, rua, numero)
    
    return address

def menu(user: Usuario):
    cidadao_repo = CidadaoRepository()
    enfermeiro_repo = EnfermeiroRepository()
    medico_repo = MedicoRepository()
    ubs_repo = Ubs_repository()
    
    limpa_telinha()
    
    if user.tipo == TipoUsuario.ADMINISTRADOR:
        while True:
            print("1 - Opções de pessoas")
            print("0 - Deslogar")
            opcao = int(input("Escolha uma opção: "))
            
            if opcao == 1:
                limpa_telinha()
                
                while True:
                    print("1 - Cidadãos")
                    print("2 - Enfermeiros")
                    print("3 - Médicos")
                    print("0 - Voltar")
                    
                    opcao1 = int(input("Escolha uma opção: "))
                    
                    if opcao1 == 1:
                        limpa_telinha()
                        
                        while True:
                            print("1 - Listar todos por ubs")
                            print("2 - Listar por número do SUS")
                            print("3 - Listar por nome")
                            print("4 - Cadastrar um novo cidadão")
                            print("0 - Voltar")

                            opcao2 = int(input("Escolha uma opcao: "))
                            
                            if opcao2 == 1:
                                nome_ubs = input("Digite o nome da ubs: ")
                                ubs = ubs_repo.search_per_name(nome_ubs)
                                
                                if ubs is None:
                                    print("Nome da UBS não existe!")
                                else:
                                    cidadaos = cidadao_repo.listar_todos_por_ubs(ubs)
                                
                                    for cidadao in cidadaos:
                                        cidadao.exibir()
                                
                            elif opcao2 == 2:
                                num_sus = int(input("Digite o número do SUS: "))
                                
                                cidadao = cidadao_repo.buscar_por_sus(num_sus)
                                
                                if cidadao is None:
                                    print("Número do SUS informado não existe!")
                                else:
                                    cidadao.exibir()
                                
                            elif opcao2 == 3:
                                nome_pessoa = input("Digite o primeiro nome ou nome completo do cidadão: ")
                                
                                cidadaos = cidadao_repo.buscar_por_nome(nome_pessoa)
                                
                                if cidadaos == []:
                                    print("Nenhum cidadão com este nome foi encontrado!")
                                else:
                                    for cidadao in cidadaos:
                                        cidadao.exibir()
                            elif opcao2 == 4:
                                cidadao = cadastrar_pessoa(Tipo.CIDADAO)
                                
                                cidadao.exibir()
                            
                            elif opcao2 == 0:
                                print("Voltando...")
                                limpa_telinha()
                                break
                    
                    elif opcao1 == 2:
                        limpa_telinha()
                        
                        while True:
                            print("1 - Listar todos por ubs")
                            print("2 - Listar por número do CIP")
                            print("3 - Cadastrar um novo enfermeiro")
                            print("0 - Voltar")
                            
                            opcao2 = int(input("Escolha uma opcao: "))
                            
                            if opcao2 == 1:
                                nome_ubs = input("Digite o nome da ubs: ")
                                ubs = ubs_repo.search_per_name(nome_ubs)
                                
                                if ubs is None:
                                    print("Nome da UBS não existe!")
                                else:
                                    enfermeiros = enfermeiro_repo.listar_enfermeiros_por_ubs(ubs)
                                
                                    for enfermeiro in enfermeiros:
                                        enfermeiro.exibir()
                            
                            elif opcao2 == 2:
                                cip = input("Digite o seu CIP: ")
                                
                                enfermeiro = enfermeiro_repo.buscar_por_cip(cip)
                                
                                if enfermeiro is None:
                                    print("CIP informado não existe!")
                                else:
                                    enfermeiro.exibir()
                            
                            elif opcao2 == 3:
                                enfermeiro = cadastrar_pessoa(Tipo.ENFERMEIRO)
                                
                                enfermeiro.exibir()
                            elif opcao2 == 0:
                                print("Voltando...")
                                limpa_telinha()
                                break
                            else:
                                print("Opção inválida!")
                    
                    elif opcao1 == 3:
                        limpa_telinha()
                        
                        while True:
                            print("1 - Listar todos por ubs")
                            print("2 - Listar por número do CRM")
                            print("3 - Cadastrar um novo médico")
                            print("0 - Voltar")
                            
                            opcao2 = int(input("Escolha uma opção: "))
                            
                            if opcao2 == 1:
                                nome_ubs = input("Digite o nome da ubs: ")
                                ubs = ubs_repo.search_per_name(nome_ubs)
                                
                                if ubs is None:
                                    print("Nome da UBS não existe!")
                                else:
                                    medicos = medico_repo.listar_medicos_por_ubs(ubs)
                                
                                    for medico in medicos:
                                        medico.exibir()
                            
                            elif opcao2 == 2:
                                crm = input("Digite o seu CRM: ")
                                
                                medico = medico_repo.buscar_por_crm(crm)
                                
                                if medico is None:
                                    print("CRM informado não existe!")
                                else:
                                    medico.exibir()
                            elif opcao2 == 3:
                                medico = cadastrar_pessoa(Tipo.MEDICO)
                                
                                medico.exibir()
                            elif opcao2 == 0:
                                print("Voltando...")
                                limpa_telinha()
                                break
                            else:
                                print("Opção inválida!")
                                limpa_telinha()
                            
                    elif opcao1 == 0:
                        print("Voltando...")
                        limpa_telinha()
                        break
                    else:
                        print("Opção inválida!")
                        limpa_telinha()
            
            elif opcao == 0:
                print("Saindo...")
                limpa_telinha()
                break
        
    elif user.tipo == TipoUsuario.CIDADAO:
        print()
    elif user.tipo == TipoUsuario.ENFERMEIRO:
        print()
    elif user.tipo == TipoUsuario.MEDICO:
        print()