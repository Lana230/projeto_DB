#Testando conexão com o banco de dados
import sqlite3

caminho = "./database/banco.db"

conexao = sqlite3.connect(caminho)

cursor = conexao.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())

conexao.commit()

conexao.close()