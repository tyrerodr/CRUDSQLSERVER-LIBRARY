# @autor: Magno Efren
# https://www.youtube.com/c/MagnoEfren

import sys
from VENTANAS.GUIDocente import * 
from DAO.DocenteDAO import *
from PyQt5.QtWidgets import QTableWidgetItem


class Docente(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.datosTotal = Registro_datos()
        self.ui.bt_refrescar.clicked.connect(self.m_productos)
        self.ui.bt_agregar.clicked.connect(self.insert_Docente)
        self.ui.bt_borrar.clicked.connect(self.eliminar_producto)
        self.ui.bt_actualizar.clicked.connect(self.modificar_Docentes)
        self.ui.id_buscar.clicked.connect(self.set_actualizarpage)
        self.ui.borrar_ok.clicked.connect(self.consultar_borrado)

        self.ui.tabla_borrar.setColumnWidth(0, 98)
        self.ui.tabla_borrar.setColumnWidth(1, 100)
        self.ui.tabla_borrar.setColumnWidth(2, 98)
        self.ui.tabla_borrar.setColumnWidth(3, 98)
        self.ui.tabla_borrar.setColumnWidth(4, 98)

        self.ui.tabla_docentes.setColumnWidth(0, 98)
        self.ui.tabla_docentes.setColumnWidth(1, 100)
        self.ui.tabla_docentes.setColumnWidth(2, 98)
        self.ui.tabla_docentes.setColumnWidth(3, 98)
        self.ui.tabla_docentes.setColumnWidth(4, 98)

    def m_productos(self):
        datos = self.datosTotal.buscar_Docente()
        i = len(datos)

        self.ui.tabla_docentes.setRowCount(i)
        tablerow = 0
        for row in datos:
            self.ui.tabla_docentes.setItem(
                tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.ui.tabla_docentes.setItem(
                tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.ui.tabla_docentes.setItem(
                tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.ui.tabla_docentes.setItem(
                tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            tablerow += 1

    def insert_Docente(self):
        idA = self.ui.idA.text()
        tercernivelA = self.ui.tercernivelA.text()
        cuartonivelA = self.ui.cuartonivelA.text()
        contador_docenteA = self.ui.contador_docenteA.text()

        self.datosTotal.inserta_Docente(
            idA, tercernivelA, cuartonivelA, contador_docenteA)

        self.ui.idA.clear()
        self.ui.tercernivelA.clear()
        self.ui.cuartonivelA.clear()
        self.ui.contador_docenteA.clear()


    def set_actualizarpage(self):
        id_docente = self.ui.id_docente.text()
        id_docente = str("'" + id_docente + "'")
        nombreXX = self.datosTotal.busca_Docente(id_docente)
        print(nombreXX)

        if nombreXX != []:
            print(self.datosTotal.busca_Docente(id_docente))
            datos = self.datosTotal.busca_Docente(id_docente)[0]
            print(datos[0])
            self.ui.id_actualizar.setText(str(datos[0]))
            self.ui.tercernivel_actualizar.setText(str(datos[1]))
            self.ui.cuartonivel_actualizar.setText(str(datos[2]))
            self.ui.contador_docente_actualizar.setText(str(datos[3]))


    def modificar_Docentes(self):
        id_docente = self.ui.id_docente.text()
        id_docente = str("'" + id_docente + "'")
        nombreXX = self.datosTotal.busca_Docente(id_docente)

        if nombreXX != None:
            self.ui.id_buscar.setText("ACTUALIZAR")
            idM = self.ui.id_actualizar.text()
            tercernivelM = self.ui.tercernivel_actualizar.text()
            cuartonivelM = self.ui.cuartonivel_actualizar.text()
            contador_docenteM = self.ui.contador_docente_actualizar.text()

            act = self.datosTotal.actualiza_Docente(
                idM, tercernivelM, cuartonivelM, contador_docenteM)
            if act == 1:
                self.ui.id_buscar.setText("ACTUALIZADO")
                self.ui.id_actualizar.clear()
                self.ui.tercernivel_actualizar.clear()
                self.ui.cuartonivel_actualizar.clear()
                self.ui.contador_docente_actualizar.clear()
                
                self.ui.id_docente.clear()

            elif act == 0:
                self.ui.id_buscar.setText("ERROR")
            else:
                self.ui.id_buscar.setText("INCORRECTO")
        else:
            self.ui.id_buscar.setText("NO EXISTE")


    def consultar_borrado(self):
        datos = self.datosTotal.buscar_Docente()
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
            self.ui.tabla_borrar.setItem(
                tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            tablerow += 1

    def eliminar_producto(self):
        eliminar = self.ui.id_borrar.text()
        eliminar = str("'" + eliminar + "'")
        resp = (self.datosTotal.elimina_Docente(eliminar))
        if resp == None:
            self.ui.borrar_ok.setText("NO EXISTE")
        elif resp == 0:
            self.ui.borrar_ok.setText("NO EXISTE")

        else:
            self.ui.borrar_ok.setText("Consultar")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mi_app = Docente()
    mi_app.show()
    sys.exit(app.exec_())
