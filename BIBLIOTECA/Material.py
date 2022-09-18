# @autor: Magno Efren
# https://www.youtube.com/c/MagnoEfren

import sys
from VENTANAS.GUIMaterial import *
from DAO.MaterialDAO import *
from PyQt5.QtWidgets import QTableWidgetItem


class Material(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.datosTotal = Registro_datos()
        self.ui.bt_refrescar.clicked.connect(self.m_productos)
        self.ui.bt_agregar.clicked.connect(self.insert_Material)
        self.ui.bt_borrar.clicked.connect(self.eliminar_producto)
        self.ui.bt_actualizar.clicked.connect(self.modificar_Materiales)
        self.ui.id_buscar.clicked.connect(self.set_actualizarpage)
        self.ui.borrar_ok.clicked.connect(self.consultar_borrado)

        self.ui.tabla_borrar.setColumnWidth(0, 98)
        self.ui.tabla_borrar.setColumnWidth(1, 100)
        self.ui.tabla_borrar.setColumnWidth(2, 98)
        self.ui.tabla_borrar.setColumnWidth(3, 98)
        self.ui.tabla_borrar.setColumnWidth(4, 98)

        self.ui.tabla_materiales.setColumnWidth(0, 98)
        self.ui.tabla_materiales.setColumnWidth(1, 100)
        self.ui.tabla_materiales.setColumnWidth(2, 98)
        self.ui.tabla_materiales.setColumnWidth(3, 98)
        self.ui.tabla_materiales.setColumnWidth(4, 98)

    def m_productos(self):
        datos = self.datosTotal.buscar_Material()
        i = len(datos)

        self.ui.tabla_materiales.setRowCount(i)
        tablerow = 0
        for row in datos:
            self.ui.tabla_materiales.setItem(
                tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.ui.tabla_materiales.setItem(
                tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.ui.tabla_materiales.setItem(
                tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.ui.tabla_materiales.setItem(
                tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            self.ui.tabla_materiales.setItem(
                tablerow, 4, QtWidgets.QTableWidgetItem(str(row[4])))
            self.ui.tabla_materiales.setItem(
                tablerow, 5, QtWidgets.QTableWidgetItem(str(row[5])))
            self.ui.tabla_materiales.setItem(
                tablerow, 6, QtWidgets.QTableWidgetItem(str(row[6])))
            self.ui.tabla_materiales.setItem(
                tablerow, 7, QtWidgets.QTableWidgetItem(str(row[7])))
            tablerow += 1

    def insert_Material(self):
        codigoA = self.ui.codigoA.text()
        autorA = self.ui.autorA.text()
        tituloA = self.ui.tituloA.text()
        anioA = self.ui.anioA.text()
        editorialA = self.ui.editorialA.text()
        disponibleA = self.ui.disponibleA.text()
        cantidad_disponibleA = self.ui.cantidad_disponibleA.text()
        ntipoA = self.ui.ntipoA.text()


        self.datosTotal.inserta_Material(
            codigoA, autorA, tituloA, anioA, editorialA ,disponibleA, cantidad_disponibleA, ntipoA)

        self.ui.codigoA.clear()
        self.ui.autorA.clear()
        self.ui.tituloA.clear()
        self.ui.anioA.clear()
        self.ui.editorialA.clear()
        self.ui.disponibleA.clear()
        self.ui.cantidad_disponibleA.clear()
        self.ui.ntipoA.clear()

    def set_actualizarpage(self):
        codigo_material = self.ui.codigo_material.text()
        codigo_material = str("'" + codigo_material + "'")
        nombreXX = self.datosTotal.busca_Material(codigo_material)
        print(nombreXX)

        if nombreXX != []:
            print(self.datosTotal.busca_Material(codigo_material))
            datos = self.datosTotal.busca_Material(codigo_material)[0]
            print(datos[0])
            self.ui.codigo_actualizar.setText(str(datos[0]))
            self.ui.autor_actualizar.setText(str(datos[1]))
            self.ui.titulo_actualizar.setText(str(datos[2]))
            self.ui.anio_actualizar.setText(str(datos[3]))
            self.ui.editorial_actualizar.setText(str(datos[4]))
            self.ui.disponible_actualizar.setText(str(datos[5]))
            self.ui.cantidad_disponible_actualizar.setText(str(datos[6]))
            self.ui.ntipo_actualizar.setText(str(datos[7]))

    def modificar_Materiales(self):
        codigo_material = self.ui.codigo_material.text()
        codigo_material = str("'" + codigo_material + "'")
        nombreXX = self.datosTotal.busca_Material(codigo_material)

        if nombreXX != None:
            self.ui.id_buscar.setText("ACTUALIZAR")
            codigoM = self.ui.codigo_actualizar.text()
            autorM = self.ui.autor_actualizar.text()
            tituloM = self.ui.titulo_actualizar.text()
            anioM = self.ui.anio_actualizar.text()
            editorialM = self.ui.editorial_actualizar.text()
            disponibleM = self.ui.disponible_actualizar.text()
            cantidad_disponibleM = self.ui.cantidad_disponible_actualizar.text()
            ntipoM = self.ui.ntipo_actualizar.text()

            act = self.datosTotal.actualiza_Material(
                codigoM, autorM, tituloM, anioM, editorialM, disponibleM, cantidad_disponibleM, ntipoM)
            if act == 1:
                self.ui.id_buscar.setText("ACTUALIZADO")
                self.ui.codigo_actualizar.clear()
                self.ui.autor_actualizar.clear()
                self.ui.titulo_actualizar.clear()
                self.ui.anio_actualizar.clear()
                self.ui.editorial_actualizar.clear()
                self.ui.disponible_actualizar.clear()
                self.ui.cantidad_disponible_actualizar.clear()
                self.ui.ntipo_actualizar.clear()
                self.ui.codigo_material.clear()

            elif act == 0:
                self.ui.id_buscar.setText("ERROR")
            else:
                self.ui.id_buscar.setText("INCORRECTO")
        else:
            self.ui.id_buscar.setText("NO EXISTE")

    def consultar_borrado(self):
        datos = self.datosTotal.buscar_Material()
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
            self.ui.tabla_borrar.setItem(
                tablerow, 4, QtWidgets.QTableWidgetItem(str(row[4])))
            self.ui.tabla_borrar.setItem(
                tablerow, 5, QtWidgets.QTableWidgetItem(str(row[5])))
            self.ui.tabla_borrar.setItem(
                tablerow, 6, QtWidgets.QTableWidgetItem(str(row[6])))
            self.ui.tabla_borrar.setItem(
                tablerow, 7, QtWidgets.QTableWidgetItem(str(row[7])))
            tablerow += 1

    def eliminar_producto(self):
        eliminar = self.ui.codigo_borrar.text()
        eliminar = str("'" + eliminar + "'")
        resp = (self.datosTotal.elimina_Material(eliminar))
        if resp == None:
            self.ui.borrar_ok.setText("NO EXISTE")
        elif resp == 0:
            self.ui.borrar_ok.setText("NO EXISTE")

        else:
            self.ui.borrar_ok.setText("Consultar")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mi_app = Material()
    mi_app.show()
    sys.exit(app.exec_())
