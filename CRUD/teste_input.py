
import sqlite3

print("Digite os dados para inserir na tabela pessoa:")
id_ubs = int(input("ID da UBS: "))
nome_pessoa = input("Nome da pessoa: ")
estado_civil = input("Estado civil: ")

dados = (id_ubs, nome_pessoa, estado_civil)

try:
    con = sqlite3.connect('database/ubs_teste.db')  # ajusta o caminho
    print("Conexão com SQLite bem-sucedida!")

    cursor = con.cursor()

    inserir_pessoa = """
    INSERT INTO pessoa (id_ubs, nome_pessoa, estado_civil)
    VALUES (?, ?, ?)
    """

    cursor.execute(inserir_pessoa, dados)

    con.commit()

    print("Registro inserido com sucesso!")

    cursor.execute("SELECT * FROM pessoa;")
    linhas = cursor.fetchall()

    print("\nNúmero total de registros:", len(linhas))
    print("\nMostrando os dados:\n")

    for linha in linhas:
        print(linha)

except sqlite3.Error as e:
    print("Erro ao acessar banco:", e)

finally:
    if 'con' in locals() and con:
        con.close()
        print("\nConexão SQLite encerrada")