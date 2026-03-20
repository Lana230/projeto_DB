from models import *

from database.conexao import connection

class Appointment_repository():
    #SALVAR CONSULTA DENTRO DO BANCO DE DADOS
    def save_appoi_db(self, appointment: Appointment):
        con = connection()
        cursor = con.cursor()

        try:
            cursor.execute(
                "INSERT INTO consulta (num_sus, crm, id_ubs, motivo, habitos_de_vida, data) VALUES (?, ?, ?, ?, ?, ?)",
                (appointment.citizen.num_sus, appointment.doctor.crm, appointment.ubs.id_ubs, appointment.reason, appointment.life_habits, appointment.date.isoformat())
            )
            
            appointment.id_appointment = cursor.lastrowid

            for h in appointment.hypothesis:
                h.save_hypothesis_db(cursor, appointment, h)

            for e in appointment.exam:
                e.save_exam_db(cursor, appointment, e)
            
            for m in appointment.medication_appoi:
                m.save_medication_appoi_db(cursor, appointment, m)

            con.commit()
        
        except Exception as e:
            con.rollback() 
            print("Erro:", e)

        finally:
            con.close()

        return appointment