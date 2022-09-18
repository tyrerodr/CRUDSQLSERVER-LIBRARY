import pyodbc


class Registro_datos():
    def __init__(self):
        self.conexion = pyodbc.connect('Driver={SQL Server};'
                                       'Server=DESKTOP-E229N4H\SQLEXPRESS;'
                                       'Database=Biblioteca;'
                                       'Trusted_Connection=yes;')

    def inserta_Libro(self, id, tipo_pasta, contador_libro):
        cur = self.conexion.cursor()
        sql = '''INSERT INTO Libro (id, tipo_pasta, contador_libro) 
        VALUES('{}', '{}','{}')'''.format(id, tipo_pasta, contador_libro)
        cur.execute(sql)
        cur.commit()
        cur.close()

    def buscar_Libro(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM Libro "
        cursor.execute(sql)
        collected_data = cursor.fetchall()
        cursor.commit()
        cursor.close()
        return collected_data

    def busca_Libro(self, id_Libro):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM Libro WHERE id = {}".format(id_Libro)
        cur.execute(sql)
        collected_data = cur.fetchall()
        cur.commit()
        cur.close()
        return collected_data

    def elimina_Libro(self, id_Libro):
        cur = self.conexion.cursor()
        sql = '''DELETE FROM Libro WHERE id = {}'''.format(id_Libro)
        cur.execute(sql)
        cur.commit()
        cur.close()
        return 1

    def actualiza_Libro(self, id, tipo_pasta, contador_libro):
        cur = self.conexion.cursor()
        sql = '''UPDATE Libro SET  id='{}',tipo_pasta='{}', contador_libro='{}'
        WHERE id = '{}' '''.format(id, tipo_pasta, contador_libro,id)
        cur.execute(sql)
        cur.commit()
        cur.close()
        return 1
