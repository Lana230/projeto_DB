from models.appointment import Appointment

from .cidadao_repository import CidadaoRepository
from .ubs_repository import Ubs_repository
from .medico_repository import MedicoRepository
from .agendamento_repository import AgendamentoRepository

import sqlite3
from database.conexao import connection

class Appointment_repository():
    def __init__(self):
        self.citizen_repo = CidadaoRepository()
        self.ubs_repo = Ubs_repository()
        self.doctor_repo = MedicoRepository()
        self.agendamento_repo = AgendamentoRepository()

    #SALVAR CONSULTA DENTRO DO BANCO DE DADOS
    def save(self, appointment: Appointment):
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
    
    def build_object(self, rows): 
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
    
    def search_per_id(self, id_appointment):
        con = connection()
        con.row_factory = sqlite3.Row
        cursor = con.cursor()

        cursor.execute(
            "SELECT * FROM consulta WHERE id_consulta = ?",
            (id_appointment,)
        )
        row = cursor.fetchone()

        con.close()

        if row is None:
            return None

        return self.build_object([row])[0]
    
    def search_all(self, doctor_crm=None, id_ubs=None, data = None, scheduling=None):
        con = connection()
        con.row_factory = sqlite3.Row
        cursor = con.cursor()

        query = "SELECT * FROM consulta"
        params = []

        if doctor_crm:
            query += " WHERE id_medico = ?"
            params.append(doctor_crm)

        if id_ubs:
            if doctor_crm:
                query += " AND id_ubs = ?"
            else:
                query += " WHERE id_ubs = ?"
            params.append(id_ubs)

        if data:
            if doctor_crm or id_ubs:
                query += " AND data = ?"
            else:
                query += " WHERE data = ?"
            params.append(data.isoformat())

        if scheduling and scheduling.cidadao and scheduling.cidadao.num_sus:
            if doctor_crm or id_ubs or data:
                query += " AND id_agendamento IN (SELECT id_agendamento FROM agendamento WHERE num_sus = ?)"
            else:
                query += " WHERE id_agendamento IN (SELECT id_agendamento FROM agendamento WHERE num_sus = ?)"
            params.append(scheduling.cidadao.num_sus)

        cursor.execute(query, tuple(params))
        rows = cursor.fetchall()

        con.close()

        return self.build_object(rows)
    
    def appointment_info(self, appointment):
        con = connection()
        con.row_factory = sqlite3.Row
        cursor = con.cursor()

        query = """
        SELECT 
            C.id_consulta,
            C.id_agendamento,
            C.id_medico,
            C.id_ubs,
            C.motivo,
            C.habitos_de_vida,
            C.data
        """
        query += " FROM consulta C"
        query += " LEFT JOIN hipotese H ON C.id_consulta = H.id_consulta"
        query += " LEFT JOIN exame E ON C.id_consulta = E.id_consulta"      
        query += " LEFT JOIN medicamento_appoi M ON C.id_consulta = M.id_consulta"
        
        query += " WHERE C.id_consulta = ?"

        cursor.execute(query, (appointment.id_appointment,))
        rows = cursor.fetchall()

        con.close()
        
        return self.build_object(rows)[0]