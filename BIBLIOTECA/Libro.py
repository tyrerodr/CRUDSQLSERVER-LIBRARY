
import sys
from VENTANAS.GUILibro import * 
from DAO.LibroDAO import *
from PyQt5.QtWidgets import QTableWidgetItem


class Libro(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.datosTotal = Registro_datos()
        self.ui.bt_refrescar.clicked.connect(self.m_productos)
        self.ui.bt_agregar.clicked.connect(self.insert_Libro)
        self.ui.bt_borrar.clicked.connect(self.eliminar_producto)
        self.ui.bt_actualizar.clicked.connect(self.modificar_Libros)
        self.ui.id_buscar.clicked.connect(self.set_actualizarpage)
        self.ui.borrar_ok.clicked.connect(self.consultar_borrado)

        self.ui.tabla_borrar.setColumnWidth(0, 98)
        self.ui.tabla_borrar.setColumnWidth(1, 100)
        self.ui.tabla_borrar.setColumnWidth(2, 98)
        self.ui.tabla_borrar.setColumnWidth(3, 98)
        self.ui.tabla_borrar.setColumnWidth(4, 98)

        self.ui.tabla_libros.setColumnWidth(0, 98)
        self.ui.tabla_libros.setColumnWidth(1, 100)
        self.ui.tabla_libros.setColumnWidth(2, 98)
        self.ui.tabla_libros.setColumnWidth(3, 98)
        self.ui.tabla_libros.setColumnWidth(4, 98)

    def m_productos(self):
        datos = self.datosTotal.buscar_Libro()
        i = len(datos)

        self.ui.tabla_libros.setRowCount(i)
        tablerow = 0
        for row in datos:
            self.ui.tabla_libros.setItem(
                tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.ui.tabla_libros.setItem(
                tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.ui.tabla_libros.setItem(
                tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            tablerow += 1

    def insert_Libro(self):
        idA = self.ui.idA.text()
        tipo_pastaA = self.ui.tipo_pastaA.text()
        contador_libroA = self.ui.contador_libroA.text()

        self.datosTotal.inserta_Libro(
            idA, tipo_pastaA, contador_libroA)

        self.ui.idA.clear()
        self.ui.tipo_pastaA.clear()
        self.ui.contador_libroA.clear()


    def set_actualizarpage(self):
        id_libro = self.ui.id_libro.text()
        id_libro = str("'" + id_libro + "'")
        nombreXX = self.datosTotal.busca_Libro(id_libro)
        print(nombreXX)

        if nombreXX != []:
            print(self.datosTotal.busca_Libro(id_libro))
            datos = self.datosTotal.busca_Libro(id_libro)[0]
            print(datos[0])
            self.ui.id_actualizar.setText(str(datos[0]))
            self.ui.tipo_pasta_actualizar.setText(str(datos[1]))
            self.ui.contador_libro_actualizar.setText(str(datos[2]))


    def modificar_Libros(self):
        id_libro = self.ui.id_libro.text()
        id_libro = str("'" + id_libro + "'")
        nombreXX = self.datosTotal.busca_Libro(id_libro)

        if nombreXX != None:
            self.ui.id_buscar.setText("ACTUALIZAR")
            idM = self.ui.id_actualizar.text()
            tipo_pastaM = self.ui.tipo_pasta_actualizar.text()
            contador_libroM = self.ui.contador_libro_actualizar.text()


            act = self.datosTotal.actualiza_Libro(
                idM, tipo_pastaM, contador_libroM)
            if act == 1:
                self.ui.id_buscar.setText("ACTUALIZADO")
                self.ui.id_actualizar.clear()
                self.ui.tipo_pasta_actualizar.clear()
                self.ui.contador_libro_actualizar.clear()
                
                self.ui.id_libro.clear()

            elif act == 0:
                self.ui.id_buscar.setText("ERROR")
            else:
                self.ui.id_buscar.setText("INCORRECTO")
        else:
            self.ui.id_buscar.setText("NO EXISTE")


    def consultar_borrado(self):
        datos = self.datosTotal.buscar_Libro()
        i = len(datos)
        self.ui.tabla_borrar.setRowCount(i)
        tablerow = 0
        for row in datos:
            self.ui.tabla_borrar.setItem(
                tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.ui.tabla_borrar.setItem(
                tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.ui.tabla_borrar.setItem(
                tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            tablerow += 1

    def eliminar_producto(self):
        eliminar = self.ui.id_borrar.text()
        eliminar = str("'" + eliminar + "'")
        resp = (self.datosTotal.elimina_Libro(eliminar))
        if resp == None:
            self.ui.borrar_ok.setText("NO EXISTE")
        elif resp == 0:
            self.ui.borrar_ok.setText("NO EXISTE")

        else:
            self.ui.borrar_ok.setText("Consultar")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mi_app = Libro()
    mi_app.show()
    sys.exit(app.exec_())
