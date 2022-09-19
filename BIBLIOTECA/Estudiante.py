import sys
from VENTANAS.GUIEstudiante import * 
from DAO.EstudianteDAO import *
from PyQt5.QtWidgets import QTableWidgetItem


class Estudiante(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.datosTotal = Registro_datos()
        self.ui.bt_refrescar.clicked.connect(self.m_productos)
        self.ui.bt_agregar.clicked.connect(self.insert_Estudiante)
        self.ui.bt_borrar.clicked.connect(self.eliminar_producto)
        self.ui.bt_actualizar.clicked.connect(self.modificar_Estudiantes)
        self.ui.id_buscar.clicked.connect(self.set_actualizarpage)
        self.ui.borrar_ok.clicked.connect(self.consultar_borrado)

        self.ui.tabla_borrar.setColumnWidth(0, 98)
        self.ui.tabla_borrar.setColumnWidth(1, 100)
        self.ui.tabla_borrar.setColumnWidth(2, 98)
        self.ui.tabla_borrar.setColumnWidth(3, 98)
        self.ui.tabla_borrar.setColumnWidth(4, 98)

        self.ui.tabla_estudiantes.setColumnWidth(0, 98)
        self.ui.tabla_estudiantes.setColumnWidth(1, 100)
        self.ui.tabla_estudiantes.setColumnWidth(2, 98)
        self.ui.tabla_estudiantes.setColumnWidth(3, 98)
        self.ui.tabla_estudiantes.setColumnWidth(4, 98)

    def m_productos(self):
        datos = self.datosTotal.buscar_Estudiante()
        i = len(datos)

        self.ui.tabla_estudiantes.setRowCount(i)
        tablerow = 0
        for row in datos:
            self.ui.tabla_estudiantes.setItem(
                tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.ui.tabla_estudiantes.setItem(
                tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.ui.tabla_estudiantes.setItem(
                tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            tablerow += 1

    def insert_Estudiante(self):
        idA = self.ui.idA.text()
        nivelA = self.ui.nivelA.text()
        contador_estudianteA = self.ui.contador_estudianteA.text()

        self.datosTotal.inserta_Estudiante(
            idA, nivelA, contador_estudianteA)

        self.ui.idA.clear()
        self.ui.nivelA.clear()
        self.ui.contador_estudianteA.clear()


    def set_actualizarpage(self):
        id_estudiante = self.ui.id_estudiante.text()
        id_estudiante = str("'" + id_estudiante + "'")
        nombreXX = self.datosTotal.busca_Estudiante(id_estudiante)
        print(nombreXX)

        if nombreXX != []:
            print(self.datosTotal.busca_Estudiante(id_estudiante))
            datos = self.datosTotal.busca_Estudiante(id_estudiante)[0]
            print(datos[0])
            self.ui.id_actualizar.setText(str(datos[0]))
            self.ui.nivel_actualizar.setText(str(datos[1]))
            self.ui.contador_estudiante_actualizar.setText(str(datos[2]))


    def modificar_Estudiantes(self):
        id_estudiante = self.ui.id_estudiante.text()
        id_estudiante = str("'" + id_estudiante + "'")
        nombreXX = self.datosTotal.busca_Estudiante(id_estudiante)

        if nombreXX != None:
            self.ui.id_buscar.setText("ACTUALIZAR")
            idM = self.ui.id_actualizar.text()
            nivelM = self.ui.nivel_actualizar.text()
            contador_estudianteM = self.ui.contador_estudiante_actualizar.text()


            act = self.datosTotal.actualiza_Estudiante(
                idM, nivelM, contador_estudianteM)
            if act == 1:
                self.ui.id_buscar.setText("ACTUALIZADO")
                self.ui.id_actualizar.clear()
                self.ui.nivel_actualizar.clear()
                self.ui.contador_estudiante_actualizar.clear()
                
                self.ui.id_estudiante.clear()

            elif act == 0:
                self.ui.id_buscar.setText("ERROR")
            else:
                self.ui.id_buscar.setText("INCORRECTO")
        else:
            self.ui.id_buscar.setText("NO EXISTE")


    def consultar_borrado(self):
        datos = self.datosTotal.buscar_Estudiante()
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
        resp = (self.datosTotal.elimina_Estudiante(eliminar))
        if resp == None:
            self.ui.borrar_ok.setText("NO EXISTE")
        elif resp == 0:
            self.ui.borrar_ok.setText("NO EXISTE")

        else:
            self.ui.borrar_ok.setText("Consultar")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mi_app = Estudiante()
    mi_app.show()
    sys.exit(app.exec_())
