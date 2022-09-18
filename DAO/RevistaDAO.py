import pyodbc


class Registro_datos():
    def __init__(self):
        self.conexion = pyodbc.connect('Driver={SQL Server};'
                                       'Server=DESKTOP-E229N4H\SQLEXPRESS;'
                                       'Database=Biblioteca;'
                                       'Trusted_Connection=yes;')

    def inserta_Revista(self, id, tipo, contador_revista):
        cur = self.conexion.cursor()
        sql = '''INSERT INTO Revista (id, tipo, contador_revista) 
        VALUES('{}', '{}','{}')'''.format(id, tipo, contador_revista)
        cur.execute(sql)
        cur.commit()
        cur.close()

    def buscar_Revista(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM Revista "
        cursor.execute(sql)
        collected_data = cursor.fetchall()
        cursor.commit()
        cursor.close()
        return collected_data

    def busca_Revista(self, id_Revista):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM Revista WHERE id = {}".format(id_Revista)
        cur.execute(sql)
        collected_data = cur.fetchall()
        cur.commit()
        cur.close()
        return collected_data

    def elimina_Revista(self, id_Revista):
        cur = self.conexion.cursor()
        sql = '''DELETE FROM Revista WHERE id = {}'''.format(id_Revista)
        cur.execute(sql)
        cur.commit()
        cur.close()
        return 1

    def actualiza_Revista(self, id, tipo, contador_revista):
        cur = self.conexion.cursor()
        sql = '''UPDATE Revista SET  id='{}',tipo='{}', contador_revista='{}'
        WHERE id = '{}' '''.format(id, tipo, contador_revista,id)
        cur.execute(sql)
        cur.commit()
        cur.close()
        return 1
