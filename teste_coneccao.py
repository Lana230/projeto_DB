# basicamnte um teste de conexão com o banco de dados para verificar se a configuração está correta e se as tabelas foram criadas com sucesso.

import sqlite3

try:
    con = sqlite3.connect('projeto_DB/database/ubs_teste.db')
    print("Conexão bem-sucedida!")
    cursor = con.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    linhas = cursor.fetchall()

    print("Tabelas no banco:", linhas)

except sqlite3.Error as e:
    print("Erro ao conectar:", e)
    
finally:
    if con:
        con.close()
        print("Conexão encerrada.")

######

######
#consulta no banco
import sqlite3

try:
    con = sqlite3.connect('projeto_DB/database/ubs_teste.db')
    print("Conexão com SQLite bem-sucedida!")

    cursor = con.cursor()

    consulta_sql = "SELECT * FROM cidadao;"
    cursor.execute(consulta_sql)

    linhas = cursor.fetchall()

    print("\nNúmero total de registros:", len(linhas))
    print("\nMostrando os dados:\n")

    for linha in linhas:
        print(linha)

except sqlite3.Error as e:
    print("Erro ao acessar banco:", e)

finally:
    if con:
        con.close()
        print("\nConexão SQLite encerrada")


#inserção de dados no banco
import sqlite3

try:
    con = sqlite3.connect('projeto_DB/database/ubs_teste.db')
    print("Conexão com SQLite bem-sucedida!")
    cursor = con.cursor()
    inserir_pessoa = """
    INSERT INTO pessoa (id_ubs, nome_pessoa, estado_civil)
    VALUES (?, ?, ?)
    """

    cursor.execute(inserir_pessoa, (765432, 'Alana Clara ', 'Solteira'))

    # ⚠️ MUITO IMPORTANTE
    con.commit()

    print("Registro inserido com sucesso!")


    consulta_sql = "SELECT * FROM pessoa;"
    cursor.execute(consulta_sql)

    linhas = cursor.fetchall()

    print("\nNúmero total de registros:", len(linhas))
    print("\nMostrando os dados:\n")

    for linha in linhas:
        print(linha)

except sqlite3.Error as e:
    print("Erro ao acessar banco:", e)

finally:
    if con:
        con.close()
        print("\nConexão SQLite encerrada")


#insercão de dados no banco com dados fornecidos por input do usuário

import sqlite3

print("Digite os dados para inserir na tabela pessoa:")
id_ubs = int(input("ID da UBS: "))
nome_pessoa = input("Nome da pessoa: ")
estado_civil = input("Estado civil: ")

dados = (id_ubs, nome_pessoa, estado_civil)

print(dados)

try:
    con = sqlite3.connect('projeto_DB/database/ubs_teste.db')
    print("Conexão com SQLite bem-sucedida!")
    cursor = con.cursor()
    inserir_pessoa = """
    INSERT INTO pessoa (id_ubs, nome_pessoa, estado_civil)
    VALUES (?, ?, ?)
    """

    cursor.execute(inserir_pessoa, dados)

    con.commit()

    print("Registro inserido com sucesso!")

    consulta_sql = "SELECT * FROM pessoa;"
    cursor.execute(consulta_sql)

    linhas = cursor.fetchall()

    print("\nNúmero total de registros:", len(linhas))
    print("\nMostrando os dados:\n")

    for linha in linhas:
        print(linha)

except sqlite3.Error as e:
    print("Erro ao acessar banco:", e)

finally:
    if con:
        con.close()
        print("\nConexão SQLite encerrada")