from models import Email

from database.conexao import connection

class EmailRepository:
    
    def salvar(self, email: Email):
        con = connection()
        cursor = con.cursor()
        
        if email.ubs is None and email.pessoa is not None:
            cursor.execute("""
                INSERT INTO email (
                    endereco_email, id_pessoa
                ) VALUES (?, ?)
                """, (
                    email.email, 
                    email.pessoa.id_pessoa
                ))
        elif email.pessoa is None and email.ubs is not None:
            cursor.execute("""
                INSERT INTO email (
                    endereco_email, id_ubs
                ) VALUES (?, ?)
                """, (
                    email.email, 
                    email.ubs.id_ubs
                ))
        
        email.id_email = cursor.lastrowid
        
        con.commit()
        con.close()
        
        return email