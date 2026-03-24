from models import *
from repositories import *

from database.conexao import connection

class Appointment_repository():
    def __init__(self):
        self.citizen_repo = CidadaoRepository()
        self.ubs_repo = Ubs_repository()
        self.doctor_repo = MedicoRepository()
        self.medication_appoi_repo = Medication_appoi_repository()
        self.exam_repo = Exam_repository()
        self.agendamento_repo = AgendamentoRepository()



    #SALVAR CONSULTA DENTRO DO BANCO DE DADOS
    def save_appoi_db(self, appointment: Appointment):
        con = connection()
        cursor = con.cursor()

        try:
            
            if appointment.scheduling and appointment.scheduling.id_agendamento:
                appointment.scheduling = self.agendamento_repo.salvar(appointment.scheduling)
            

            cursor.execute(
                "INSERT INTO consulta (id_agendamento, crm, id_ubs, motivo, habitos_de_vida, data) VALUES (?, ?, ?, ?, ?, ?)",
                (appointment.scheduling.id_agendamento, appointment.doctor.crm, appointment.ubs.id_ubs, appointment.reason, appointment.life_habits, appointment.data.isoformat())
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
    
    def build_object_appoi(self, rows): 
        appointments = []

        for row in rows:
            if row is None:
                continue   

            appois = Appointment(
                scheduling =  self.agendamento_repo.buscar_por_id(row["id_agendamento"]),
                doctor = self.doctor_repo.buscar_por_crm(row["id_medico"]),
                ubs = self.ubs_repo.search_per_id(row["id_ubs"]),
                data = row["data"],
                reason = row["motivo"],
                life_habits = row["habitos_de_vida"],
            )
            
            appois.id_appointment = row["id_consulta"]
            
            appointments.append(appois)
        
        return appointments
