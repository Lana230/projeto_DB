from models.fila_atendimento import Fila_atendimento

from database.conexao import connection

class FilaRepository:
    
    def salvar(self, fila: Fila_atendimento):
        con = connection()
        cursor = con.cursor()
        
        if fila.vacina is None and fila.medico is not None:
            cursor.execute("""
                INSERT INTO fila (
                    data_fila, id_ubs, tipo_atendimento, quantidade_maxima,
                    crm
                ) VALUES (?, ?, ?, ?)
                """, (
                    fila.data_fila, 
                    fila.ubs.id_ubs,
                    fila.tipo_atendimento.value,
                    fila.quantidade_maxima,
                    fila.medico.crm
                ))
        elif fila.medico is None and fila.vacina is not None:
            cursor.execute("""
                INSERT INTO fila (
                    data_fila, id_ubs, tipo_atendimento, quantidade_maxima,
                    id_vacina
                ) VALUES (?, ?, ?, ?)
                """, (
                    fila.data_fila,
                    fila.ubs.id_ubs,
                    fila.tipo_atendimento.value,
                    fila.quantidade_maxima,
                    fila.vacina.id_vaccine
                ))
        
        fila.id_fila = cursor.lastrowid
        
        con.commit()
        con.close()
        
        return fila