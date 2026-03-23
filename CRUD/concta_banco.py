import sqlite3

def conectar_banco():
    try:
        con = sqlite3.connect('../database/ubs_teste.db')  
        print("Conexão com SQLite bem-sucedida!")
        return con
    except sqlite3.Error as e:
        print("Erro ao acessar banco:", e)
        return None