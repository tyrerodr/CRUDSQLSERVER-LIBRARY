import pyodbc


class Registro_datos():
    def __init__(self):
        self.conexion = pyodbc.connect('Driver={SQL Server};'
                                       'Server=DESKTOP-E229N4H\SQLEXPRESS;'
                                       'Database=Biblioteca;'
                                       'Trusted_Connection=yes;')

    def inserta_Docente(self, id, titulo_3er_nivel, titulo_4_nivel, contador_docente):
        cur = self.conexion.cursor()
        sql = '''INSERT INTO Docente (id, titulo_3er_nivel, titulo_4_nivel, contador_docente) 
        VALUES('{}', '{}','{}', '{}')'''.format(id, titulo_3er_nivel, titulo_4_nivel, contador_docente)
        cur.execute(sql)
        cur.commit()
        cur.close()

    def buscar_Docente(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM Docente "
        cursor.execute(sql)
        collected_data = cursor.fetchall()
        cursor.commit()
        cursor.close()
        return collected_data

    def busca_Docente(self, id_docente):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM Docente WHERE id = {}".format(id_docente)
        cur.execute(sql)
        collected_data = cur.fetchall()
        cur.commit()
        cur.close()
        return collected_data

    def elimina_Docente(self, id_docente):
        cur = self.conexion.cursor()
        sql = '''DELETE FROM Docente WHERE id = {}'''.format(id_docente)
        cur.execute(sql)
        cur.commit()
        cur.close()
        return 1

    def actualiza_Docente(self, id, titulo_3er_nivel, titulo_4_nivel, contador_docente):
        cur = self.conexion.cursor()
        sql = '''UPDATE Docente SET  id='{}',titulo_3er_nivel='{}', titulo_4_nivel='{}', contador_docente='{}'
        WHERE id = '{}' '''.format(id, titulo_3er_nivel, titulo_4_nivel, contador_docente,id)
        cur.execute(sql)
        cur.commit()
        cur.close()
        return 1
