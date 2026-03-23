from models import Documento, TipoDocumento
from database.conexao import connection

class DocumentoRepository:
    
    def salvar(self, documento: Documento):
        con = connection()
        cursor = con.cursor()
        
        cursor.execute("""
            INSERT INTO documento (
                tipo_documento, numero_documento, id_pessoa
            ) VALUES (?, ?, ?)
            """, (
                documento.tipo_documento.value,
                documento.numero_documento,
                documento.id_pessoa
            ))
        
        documento.id_documento = cursor.lastrowid
        
        con.commit()
        con.close()
        
        return documento
    
    def construir_objeto(self, rows):
        documentos = []
        
        for row in rows:
            if row is None:
                continue
            
            documento = Documento(
                tipo_documento=TipoDocumento(row["tipo_documento"]),
                numero_documento=row["numero_documento"]
            )
            
            documento.id_documento = row["id_documento"]
            documento.id_pessoa = row["id_pessoa"]
            
            documentos.append(documento)
        
        return documentos