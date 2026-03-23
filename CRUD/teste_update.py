#atualizaçao de dados no banco
from concta_banco import conectar_banco
import sqlite3

def consulta_pessoa(id_pessoa):
    con = conectar_banco()

    if con is None:
        print("Falha na conexão com o banco.")
        return
   
    try: 
        cursor = con.cursor()
        consulta_sql = "SELECT * FROM pessoa WHERE id_pessoa = ?;"
        
        cursor.execute(consulta_sql, (id_pessoa,))

        linhas= cursor.fetchall()
        print("\nNúmero total de registros:", len(linhas))
        for linha in linhas:
            print("ID:", linha[0], 
                  "\nNome:", linha[1],
                    "\nEstado Civil:", linha[2])

    except sqlite3.Error as e:
        print("falha ao consultar tabela:", e)
        
    
    finally:
        if con:
            con.close()
            print("Conexão fechada")

def alterar_nome_pessoa(id_pessoa, novo_nome):
    con = conectar_banco()

    if con is None:
        print("Falha na conexão com o banco.")
        return
    try:
        cursor = con.cursor()

        cursor.execute("UPDATE pessoa SET nome_pessoa = ? WHERE id_pessoa = ?", (novo_nome, id_pessoa))

        con.commit()

        if cursor.rowcount == 0:
            print("Nenhum registro encontrado com esse ID.")
        else:
            print("Registro atualizado com sucesso!")
    except sqlite3.Error as e:
        print("falha ao atualizar registro:", e)
    finally:
        if con:
            con.close()
            print("Conexão fechada")


if __name__ == "__main__":
    print("insira o id da pessoa que deseja atualizar:")
    id_pessoa = int(input())
    consulta_pessoa(id_pessoa)

    print("insira o novo nome da pessoa:")
    novo_nome = input()

    alterar_nome_pessoa(id_pessoa, novo_nome)
