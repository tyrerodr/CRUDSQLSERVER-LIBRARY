import pyodbc


class Registro_datos():
    def __init__(self):
        self.conexion = pyodbc.connect('Driver={SQL Server};'
                                       'Server=DESKTOP-E229N4H\SQLEXPRESS;'
                                       'Database=Biblioteca;'
                                       'Trusted_Connection=yes;')

    def inserta_Estudiante(self, id, nivel, contador_estudiante):
        cur = self.conexion.cursor()
        sql = '''INSERT INTO Estudiante (id, nivel, contador_estudiante) 
        VALUES('{}', '{}','{}')'''.format(id, nivel, contador_estudiante)
        cur.execute(sql)
        cur.commit()
        cur.close()

    def buscar_Estudiante(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM Estudiante "
        cursor.execute(sql)
        collected_data = cursor.fetchall()
        cursor.commit()
        cursor.close()
        return collected_data

    def busca_Estudiante(self, id_estudiante):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM Estudiante WHERE id = {}".format(id_estudiante)
        cur.execute(sql)
        collected_data = cur.fetchall()
        cur.commit()
        cur.close()
        return collected_data

    def elimina_Estudiante(self, id_estudiante):
        cur = self.conexion.cursor()
        sql = '''DELETE FROM Estudiante WHERE id = {}'''.format(id_estudiante)
        cur.execute(sql)
        cur.commit()
        cur.close()
        return 1

    def actualiza_Estudiante(self, id, nivel, contador_estudiante):
        cur = self.conexion.cursor()
        sql = '''UPDATE Estudiante SET  id='{}',nivel='{}', contador_estudiante='{}'
        WHERE id = '{}' '''.format(id, nivel, contador_estudiante,id)
        cur.execute(sql)
        cur.commit()
        cur.close()
        return 1
