import pyodbc


class Registro_datos():
    def __init__(self):
        self.conexion = pyodbc.connect('Driver={SQL Server};'
                                       'Server=DESKTOP-E229N4H\SQLEXPRESS;'
                                       'Database=Biblioteca;'
                                       'Trusted_Connection=yes;')

    def inserta_persona(self, cedula, nombres, apellidos, email, telefono, direccion, numero_libros, activo, carrera, rol):
        cur = self.conexion.cursor()
        sql = '''INSERT INTO Persona (cedula, nombres, apellidos, email, telefono, direccion, numero_libros, activo, carrera, rol) 
        VALUES('{}', '{}','{}', '{}','{}','{}', '{}','{}', '{}','{}')'''.format(cedula, nombres, apellidos, email, telefono, direccion, numero_libros, activo, carrera, rol)
        cur.execute(sql)
        cur.commit()
        cur.close()

    def buscar_Persona(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM Persona "
        cursor.execute(sql)
        collected_data = cursor.fetchall()
        cursor.commit()
        cursor.close()
        return collected_data

    def busca_persona(self, cedula_persona):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM Persona WHERE cedula = {}".format(cedula_persona)
        cur.execute(sql)
        collected_data = cur.fetchall()
        cur.commit()
        cur.close()
        return collected_data

    def elimina_Persona(self, cedula_persona):
        cur = self.conexion.cursor()
        sql = '''DELETE FROM Persona WHERE cedula = {}'''.format(cedula_persona)
        cur.execute(sql)
        cur.commit()
        cur.close()
        return 1

    def actualiza_Persona(self, cedula, nombres, apellidos, email, telefono, direccion, numero_libros, activo, carrera, rol):
        cur = self.conexion.cursor()
        sql = '''UPDATE Persona SET  cedula='{}',nombres='{}', apellidos='{}', email='{}',  telefono='{}', direccion='{}', numero_libros='{}', activo='{}', carrera='{}',rol='{}'
        WHERE cedula = '{}' '''.format(cedula, nombres, apellidos, email, telefono, direccion, int(numero_libros), activo, carrera,rol, cedula)
        cur.execute(sql)
        cur.commit()
        cur.close()
        return 1
