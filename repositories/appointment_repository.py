from models import *

from database.conexao import connection

class Appointment_repository():
    #SALVAR CONSULTA DENTRO DO BANCO DE DADOS
    def save_appoi_db(self, appointment: Appointment):
        con = connection()
        cursor = con.cursor()

        try:
            cursor.execute(
                "INSERT INTO consulta (num_sus, crm, id_ubs, data, motivo, habitos_de_vida) VALUES (?, ?, ?, ?, ?, ?)",
                (appointment.citizen.num_sus, appointment.doctor.crm, appointment.ubs.id_ubs, appointment.date.isoformat(), appointment.reason, appointment.life_habits)
            )
            
            appointment.id_appointment = cursor.lastrowid
            con.commit()

            for h in appointment.hypothesis:
                h.save_hypothesis_db(cursor, appointment, h)

            for e in appointment.exam:
                e.save_exam_db(cursor, appointment, e)
            
            for m in appointment.medication_appoi:
                m.save_medication_appoi_db(cursor, appointment, m)
        
        except Exception as e:
            con.rollback() 
            print("Erro:", e)

        finally:
            con.close()

        return appointment