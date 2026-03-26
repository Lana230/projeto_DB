from models import *
from repositories import *

def criar_usuario():
    usuario_repo = Usuario_repository()
    ubs_repo = Ubs_repository()

    print("\n--- CRIAR USUÁRIO ---")

    nome_usuario = input("Nome de usuário: ")
    email = input("Email: ")
    senha = input("Senha: ")
    nome_ubs = int(input("Nome da ubs: "))
    
    while True:
        print("Tipo de usuário: ")
        print(f"1 - {TipoUsuario.ADMINISTRADOR.value}")
        print(f"2 - {TipoUsuario.CIDADAO.value}")
        print(f"3 - {TipoUsuario.ENFERMEIRO.value}")
        print(f"4 - {TipoUsuario.MEDICO.value}")
        
        opcao = input("Escolha uma opção: ")
        opcao = int(opcao)
        
        if opcao == 1:
            tipo = TipoUsuario.ADMINISTRADOR
            break
        elif opcao == 2:
            tipo = TipoUsuario.CIDADAO
            break
        elif opcao == 3:
            tipo = TipoUsuario.ENFERMEIRO
            break
        elif opcao == 4:
            tipo = TipoUsuario.MEDICO
            break
        else:
            print("Opção inválida!")
    
    ubs = ubs_repo.search_per_name(nome_ubs)

    usuario = Usuario(ubs, nome_usuario, email, senha, tipo)

    try:
        usuario_repo.salvar(usuario)
        print("Usuário criado com sucesso!")
    except Exception as e:
        print(f"Erro ao criar usuário: {e}")
    
def iniciar():
    usuario_repo = Usuario_repository()

    print("\n--- LOGIN ---")

    email = input("Email: ")
    senha = input("Senha: ")

    user = usuario_repo.buscar_por_login(email)

    if user is None:
        print("Usuário não encontrado.")
        return

    if user.senha != senha:
        print("Senha incorreta.")
        return

    print(f"Bem-vindo, {user.nome_usuario}!")
    
    # Aqui você pode redirecionar para outro menu
    #menu_sistema(user)

def menu_principal():
    while True:
        print("\n===== SISTEMA UBS =====")
        print("1 - Entrar")
        print("2 - Criar usuário")
        print("0 - Sair")
        
        opcao = input("Escolha uma opção: ")
        opcao = int(opcao)
        
        if opcao == 1:
            iniciar()
        elif opcao == 2:
            criar_usuario()
        elif opcao == 0:
            print("Saindo...")
            break
        else:
            print("Opção inválida!")