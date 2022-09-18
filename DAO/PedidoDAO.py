import pyodbc


class Registro_datos():
    def __init__(self):
        self.conexion = pyodbc.connect('Driver={SQL Server};'
                                       'Server=DESKTOP-E229N4H\SQLEXPRESS;'
                                       'Database=Biblioteca;'
                                       'Trusted_Connection=yes;')

    def inserta_Pedido(self, id, solicitante, lista_material, materia,fecha_prestamo,fecha_devolucion,contador_pedido):
        cur = self.conexion.cursor()
        sql = '''INSERT INTO Pedido (id, solicitante, lista_material, materia,fecha_prestamo,fecha_devolucion,contador_pedido) 
        VALUES('{}', '{}','{}', '{}','{}','{}')'''.format(id, solicitante, lista_material, materia,fecha_prestamo,fecha_devolucion,contador_pedido)
        cur.execute(sql)
        cur.commit()
        cur.close()

    def buscar_Pedido(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM Pedido "
        cursor.execute(sql)
        collected_data = cursor.fetchall()
        cursor.commit()
        cursor.close()
        return collected_data

    def busca_Pedido(self, id_pedido):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM Pedido WHERE id = {}".format(id_pedido)
        cur.execute(sql)
        collected_data = cur.fetchall()
        cur.commit()
        cur.close()
        return collected_data

    def elimina_Pedido(self, id_pedido):
        cur = self.conexion.cursor()
        sql = '''DELETE FROM Pedido WHERE id = {}'''.format(id_pedido)
        cur.execute(sql)
        cur.commit()
        cur.close()
        return 1

    def actualiza_Pedido(self, id, solicitante, lista_material, materia,fecha_prestamo,fecha_devolucion,contador_pedido):
        cur = self.conexion.cursor()
        sql = '''UPDATE Pedido SET  id='{}',solicitante='{}', lista_material='{}', materia='{}',  fecha_prestamo='{}', fecha_devolucion='{}', contador_pedido='{}'
        WHERE id = '{}' '''.format(id, solicitante, lista_material, materia,fecha_prestamo,fecha_devolucion,contador_pedido, id)
        cur.execute(sql)
        cur.commit()
        cur.close()
        return 1
