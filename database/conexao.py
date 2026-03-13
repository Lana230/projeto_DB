#Testando conexão com o banco de dados
import sqlite3

caminho = "./database/banco.db"

def conection():
    return sqlite3.connect(caminho)

con = conection()

cursor = con.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())

con.commit()

con.close()