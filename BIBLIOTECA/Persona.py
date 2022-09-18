# @autor: Magno Efren
# https://www.youtube.com/c/MagnoEfren

import sys
from VENTANAS.GUIPersona import * 
from DAO.PersonaDAO import *
from PyQt5.QtWidgets import QTableWidgetItem


class Persona(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.datosTotal = Registro_datos()
        self.ui.bt_refrescar.clicked.connect(self.m_productos)
        self.ui.bt_agregar.clicked.connect(self.insert_persona)
        self.ui.bt_borrar.clicked.connect(self.eliminar_producto)
        self.ui.bt_actualizar.clicked.connect(self.modificar_personas)
        self.ui.id_buscar.clicked.connect(self.set_actualizarpage)
        self.ui.borrar_ok.clicked.connect(self.consultar_borrado)

        self.ui.tabla_borrar.setColumnWidth(0, 98)
        self.ui.tabla_borrar.setColumnWidth(1, 100)
        self.ui.tabla_borrar.setColumnWidth(2, 98)
        self.ui.tabla_borrar.setColumnWidth(3, 98)
        self.ui.tabla_borrar.setColumnWidth(4, 98)

        self.ui.tabla_personas.setColumnWidth(0, 98)
        self.ui.tabla_personas.setColumnWidth(1, 100)
        self.ui.tabla_personas.setColumnWidth(2, 98)
        self.ui.tabla_personas.setColumnWidth(3, 98)
        self.ui.tabla_personas.setColumnWidth(4, 98)

    def m_productos(self):
        datos = self.datosTotal.buscar_Persona()
        i = len(datos)

        self.ui.tabla_personas.setRowCount(i)
        tablerow = 0
        for row in datos:
            self.ui.tabla_personas.setItem(
                tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.ui.tabla_personas.setItem(
                tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui.tabla_personas.setItem(
                tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.ui.tabla_personas.setItem(
                tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.ui.tabla_personas.setItem(
                tablerow, 4, QtWidgets.QTableWidgetItem(row[4]))
            self.ui.tabla_personas.setItem(
                tablerow, 5, QtWidgets.QTableWidgetItem(row[5]))
            self.ui.tabla_personas.setItem(
                tablerow, 6, QtWidgets.QTableWidgetItem(str(row[6])))
            self.ui.tabla_personas.setItem(
                tablerow, 7, QtWidgets.QTableWidgetItem(str(row[7])))
            self.ui.tabla_personas.setItem(
                tablerow, 8, QtWidgets.QTableWidgetItem(row[8]))
            self.ui.tabla_personas.setItem(
                tablerow, 9, QtWidgets.QTableWidgetItem(str(row[9])))
            tablerow += 1

    def insert_persona(self):
        cedulaA = self.ui.cedulaA.text()
        nombresA = self.ui.nombresA.text()
        apellidosA = self.ui.apellidosA.text()
        emailA = self.ui.emailA.text()
        telefonoA = self.ui.telefonoA.text()
        direccionA = self.ui.direccionA.text()
        numero_librosA = self.ui.numero_librosA.text()
        activoA = self.ui.activoA.text()
        carreraA = self.ui.carreraA.text()
        rolA = self.ui.rolA.text()

        self.datosTotal.inserta_persona(
            cedulaA, nombresA, apellidosA, emailA, telefonoA, direccionA, numero_librosA, activoA, carreraA, rolA)

        self.ui.cedulaA.clear()
        self.ui.nombresA.clear()
        self.ui.apellidosA.clear()
        self.ui.emailA.clear()
        self.ui.telefonoA.clear()
        self.ui.direccionA.clear()
        self.ui.numero_librosA.clear()
        self.ui.activoA.clear()
        self.ui.carreraA.clear()
        self.ui.rolA.clear()

    def set_actualizarpage(self):
        cedula_persona = self.ui.cedula_persona.text()
        cedula_persona = str("'" + cedula_persona + "'")
        nombreXX = self.datosTotal.busca_persona(cedula_persona)
        print(nombreXX)

        if nombreXX != []:
            print(self.datosTotal.busca_persona(cedula_persona))
            datos = self.datosTotal.busca_persona(cedula_persona)[0]
            print(datos[0])
            self.ui.cedula_actualizar.setText(str(datos[0]))
            self.ui.nombres_actualizar.setText(str(datos[1]))
            self.ui.apellidos_actualizar.setText(str(datos[2]))
            self.ui.email_actualizar.setText(str(datos[3]))
            self.ui.telefono_actualizar.setText(str(datos[4]))
            self.ui.direccion_actualizar.setText(str(datos[5]))
            self.ui.numero_libros_actualizar.setText(str(datos[6]))
            self.ui.activo_actualizar.setText(str(datos[7]))
            self.ui.carrera_actualizar.setText(str(datos[8]))
            self.ui.rol_actualizar.setText(str(datos[9]))

    def modificar_personas(self):
        cedula_persona = self.ui.cedula_persona.text()
        cedula_persona = str("'" + cedula_persona + "'")
        nombreXX = self.datosTotal.busca_persona(cedula_persona)

        if nombreXX != None:
            self.ui.id_buscar.setText("ACTUALIZAR")
            cedulaM = self.ui.cedula_actualizar.text()
            nombresM = self.ui.nombres_actualizar.text()
            apellidosM = self.ui.apellidos_actualizar.text()
            emailM = self.ui.email_actualizar.text()
            telefonoM = self.ui.telefono_actualizar.text()
            direccionM = self.ui.direccion_actualizar.text()
            numero_librosM = self.ui.numero_libros_actualizar.text()
            activoM = self.ui.activo_actualizar.text()
            carreraM = self.ui.carrera_actualizar.text()
            rolM = self.ui.rol_actualizar.text()

            act = self.datosTotal.actualiza_Persona(
                cedulaM, nombresM, apellidosM, emailM, telefonoM, direccionM, numero_librosM, activoM, carreraM, rolM)
            if act == 1:
                self.ui.id_buscar.setText("ACTUALIZADO")
                self.ui.cedula_actualizar.clear()
                self.ui.nombres_actualizar.clear()
                self.ui.apellidos_actualizar.clear()
                self.ui.email_actualizar.clear()
                self.ui.telefono_actualizar.clear()
                self.ui.direccion_actualizar.clear()
                self.ui.numero_libros_actualizar.clear()
                self.ui.activo_actualizar.clear()
                self.ui.carrera_actualizar.clear()
                self.ui.telefono_actualizar.clear()
                self.ui.rol_actualizar.clear()
                self.ui.cedula_persona.clear()

            elif act == 0:
                self.ui.id_buscar.setText("ERROR")
            else:
                self.ui.id_buscar.setText("INCORRECTO")
        else:
            self.ui.id_buscar.setText("NO EXISTE")


    def consultar_borrado(self):
        datos = self.datosTotal.buscar_Persona()
        i = len(datos)
        self.ui.tabla_borrar.setRowCount(i)
        tablerow = 0
        for row in datos:
            self.ui.tabla_borrar.setItem(
                tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.ui.tabla_borrar.setItem(
                tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui.tabla_borrar.setItem(
                tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.ui.tabla_borrar.setItem(
                tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.ui.tabla_borrar.setItem(
                tablerow, 4, QtWidgets.QTableWidgetItem(row[4]))
            self.ui.tabla_borrar.setItem(
                tablerow, 5, QtWidgets.QTableWidgetItem(row[5]))
            self.ui.tabla_borrar.setItem(
                tablerow, 6, QtWidgets.QTableWidgetItem(str(row[6])))
            self.ui.tabla_borrar.setItem(
                tablerow, 7, QtWidgets.QTableWidgetItem(str(row[7])))
            self.ui.tabla_borrar.setItem(
                tablerow, 8, QtWidgets.QTableWidgetItem(row[8]))
            self.ui.tabla_borrar.setItem(
                tablerow, 9, QtWidgets.QTableWidgetItem(str(row[9])))
            tablerow += 1

    def eliminar_producto(self):
        eliminar = self.ui.cedula_borrar.text()
        eliminar = str("'" + eliminar + "'")
        resp = (self.datosTotal.elimina_Persona(eliminar))
        if resp == None:
            self.ui.borrar_ok.setText("NO EXISTE")
        elif resp == 0:
            self.ui.borrar_ok.setText("NO EXISTE")

        else:
            self.ui.borrar_ok.setText("Consultar")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mi_app = Persona()
    mi_app.show()
    sys.exit(app.exec_())
