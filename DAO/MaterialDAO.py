import pyodbc


class Registro_datos():
    def __init__(self):
        self.conexion = pyodbc.connect('Driver={SQL Server};'
                                       'Server=DESKTOP-E229N4H\SQLEXPRESS;'
                                       'Database=Biblioteca;'
                                       'Trusted_Connection=yes;')

    def inserta_Material(self, codigo, autor,titulo,anio,editorial,disponible,cantidad_disponible,ntipo):
        cur = self.conexion.cursor()
        sql = '''INSERT INTO Material (codigo, autor,titulo,anio,editorial,disponible,cantidad_disponible,ntipo) 
        VALUES('{}', '{}','{}', '{}','{}','{}', '{}', '{}')'''.format(codigo, autor,titulo,anio,editorial,disponible,cantidad_disponible,ntipo)
        cur.execute(sql)
        cur.commit()
        cur.close()

    def buscar_Material(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM Material "
        cursor.execute(sql)
        collected_data = cursor.fetchall()
        cursor.commit()
        cursor.close()
        return collected_data

    def busca_Material(self, codigo_material):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM Material WHERE codigo = {}".format(codigo_material)
        cur.execute(sql)
        collected_data = cur.fetchall()
        cur.commit()
        cur.close()
        return collected_data

    def elimina_Material(self, codigo_material):
        cur = self.conexion.cursor()
        sql = '''DELETE FROM Material WHERE codigo = {}'''.format(codigo_material)
        cur.execute(sql)
        cur.commit()
        cur.close()
        return 1

    def actualiza_Material(self, codigo,autor,titulo,anio,editorial,disponible,cantidad_disponible,ntipo):
        cur = self.conexion.cursor()
        sql = '''UPDATE Material SET  codigo='{}',autor='{}', titulo='{}', anio='{}',  editorial='{}', disponible='{}', cantidad_disponible='{}',ntipo='{}'
        WHERE codigo = '{}' '''.format(codigo, autor,titulo,anio,editorial,disponible,cantidad_disponible,ntipo,codigo)
        cur.execute(sql)
        cur.commit()
        cur.close()
        return 1
