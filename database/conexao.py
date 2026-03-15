#Testando conexão com o banco de dados
import sqlite3

caminho = "./database/ubs_teste.db"

def connection():
    return sqlite3.connect(caminho)

def listar_tabelas():
    #Cria a conexão com o banco de dados
    con = connection()

    #Cria um cursor para realizar comandos em SQL
    cursor = con.cursor()

    #Executa comandos em SQL
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

    #Obtém o resultado da consulta em um array
    tabelas = cursor.fetchall()

    #Encerra a conexão com o banco de dados
    con.close()
    
    return tabelas