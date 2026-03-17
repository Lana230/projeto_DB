from database.conexao import connection
con = connection()
cursor = con.cursor()

class Medication:
    def __init__(self, name_medication, category_med):
        self.id_medication = None
        self.name_medication = name_medication
        self.category_med = category_med
    
    def save_medication_db(self):
        cursor.execute(
            "INSERT INTO medicamentos(nome_medicamento, categoria_med) VALUES (?, ?)",
            (self.name_medication, self.category_med)
        )

        self.id_medication = cursor.lastrowid