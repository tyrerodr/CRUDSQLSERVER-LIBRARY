# @autor: Magno Efren
# https://www.youtube.com/c/MagnoEfren

import sys
from VENTANAS.GUIPedido import * 
from DAO.PedidoDAO import *
from PyQt5.QtWidgets import QTableWidgetItem


class Pedido(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.datosTotal = Registro_datos()
        self.ui.bt_refrescar.clicked.connect(self.m_productos)
        self.ui.bt_agregar.clicked.connect(self.insert_Pedido)
        self.ui.bt_borrar.clicked.connect(self.eliminar_producto)
        self.ui.bt_actualizar.clicked.connect(self.modificar_Pedidos)
        self.ui.id_buscar.clicked.connect(self.set_actualizarpage)
        self.ui.borrar_ok.clicked.connect(self.consultar_borrado)

        self.ui.tabla_borrar.setColumnWidth(0, 98)
        self.ui.tabla_borrar.setColumnWidth(1, 100)
        self.ui.tabla_borrar.setColumnWidth(2, 98)
        self.ui.tabla_borrar.setColumnWidth(3, 98)
        self.ui.tabla_borrar.setColumnWidth(4, 98)

        self.ui.tabla_pedidos.setColumnWidth(0, 98)
        self.ui.tabla_pedidos.setColumnWidth(1, 100)
        self.ui.tabla_pedidos.setColumnWidth(2, 98)
        self.ui.tabla_pedidos.setColumnWidth(3, 98)
        self.ui.tabla_pedidos.setColumnWidth(4, 98)

    def m_productos(self):
        datos = self.datosTotal.buscar_Pedido()
        i = len(datos)

        self.ui.tabla_pedidos.setRowCount(i)
        tablerow = 0
        for row in datos:
            self.ui.tabla_pedidos.setItem(
                tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.ui.tabla_pedidos.setItem(
                tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.ui.tabla_pedidos.setItem(
                tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.ui.tabla_pedidos.setItem(
                tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            self.ui.tabla_pedidos.setItem(
                tablerow, 4, QtWidgets.QTableWidgetItem(str(row[4])))
            self.ui.tabla_pedidos.setItem(
                tablerow, 5, QtWidgets.QTableWidgetItem(str(row[5])))
            self.ui.tabla_pedidos.setItem(
                tablerow, 6, QtWidgets.QTableWidgetItem(str(row[6])))
            tablerow += 1

    def insert_Pedido(self):
        idA = self.ui.idA.text()
        solicitanteA = self.ui.solicitanteA.text()
        lista_materialA = self.ui.lista_materialA.text()
        materiaA = self.ui.materiaA.text()
        fecha_prestamoA = self.ui.fecha_prestamoA.text()
        fecha_devolucionA = self.ui.fecha_devolucionA.text()
        contador_pedidoA = self.ui.contador_pedidoA.text()
        activoA = self.ui.activoA.text()
        carreraA = self.ui.carreraA.text()
        rolA = self.ui.rolA.text()

        self.datosTotal.inserta_Pedido(
            idA, solicitanteA, lista_materialA, materiaA, fecha_prestamoA, fecha_devolucionA, contador_pedidoA)

        self.ui.idA.clear()
        self.ui.solicitanteA.clear()
        self.ui.lista_materialA.clear()
        self.ui.materiaA.clear()
        self.ui.fecha_prestamoA.clear()
        self.ui.fecha_devolucionA.clear()
        self.ui.contador_pedidoA.clear()

    def set_actualizarpage(self):
        id_pedido = self.ui.id_pedido.text()
        id_pedido = str("'" + id_pedido + "'")
        nombreXX = self.datosTotal.busca_Pedido(id_pedido)
        print(nombreXX)

        if nombreXX != []:
            print(self.datosTotal.busca_Pedido(id_pedido))
            datos = self.datosTotal.busca_Pedido(id_pedido)[0]
            print(datos[0])
            self.ui.id_actualizar.setText(str(datos[0]))
            self.ui.solicitante_actualizar.setText(str(datos[1]))
            self.ui.lista_material_actualizar.setText(str(datos[2]))
            self.ui.materia_actualizar.setText(str(datos[3]))
            self.ui.fecha_prestamo_actualizar.setText(str(datos[4]))
            self.ui.fecha_devolucion_actualizar.setText(str(datos[5]))
            self.ui.contador_pedido_actualizar.setText(str(datos[6]))

    def modificar_Pedidos(self):
        id_pedido = self.ui.id_pedido.text()
        id_pedido = str("'" + id_pedido + "'")
        nombreXX = self.datosTotal.busca_Pedido(id_pedido)

        if nombreXX != None:
            self.ui.id_buscar.setText("ACTUALIZAR")
            idM = self.ui.id_actualizar.text()
            solicitanteM = self.ui.solicitante_actualizar.text()
            lista_materialM = self.ui.lista_material_actualizar.text()
            materiaM = self.ui.materia_actualizar.text()
            fecha_prestamoM = self.ui.fecha_prestamo_actualizar.text()
            fecha_devolucionM = self.ui.fecha_devolucion_actualizar.text()
            contador_pedidoM = self.ui.contador_pedido_actualizar.text()


            act = self.datosTotal.actualiza_Pedido(
                idM, solicitanteM, lista_materialM, materiaM, fecha_prestamoM, fecha_devolucionM, contador_pedidoM)
            if act == 1:
                self.ui.id_buscar.setText("ACTUALIZADO")
                self.ui.id_actualizar.clear()
                self.ui.solicitante_actualizar.clear()
                self.ui.lista_material_actualizar.clear()
                self.ui.materia_actualizar.clear()
                self.ui.fecha_prestamo_actualizar.clear()
                self.ui.fecha_devolucion_actualizar.clear()
                self.ui.contador_pedido_actualizar.clear()
                self.ui.id_pedido.clear()

            elif act == 0:
                self.ui.id_buscar.setText("ERROR")
            else:
                self.ui.id_buscar.setText("INCORRECTO")
        else:
            self.ui.id_buscar.setText("NO EXISTE")


    def consultar_borrado(self):
        datos = self.datosTotal.buscar_Pedido()
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
            tablerow += 1

    def eliminar_producto(self):
        eliminar = self.ui.id_borrar.text()
        eliminar = str("'" + eliminar + "'")
        resp = (self.datosTotal.elimina_Pedido(eliminar))
        if resp == None:
            self.ui.borrar_ok.setText("NO EXISTE")
        elif resp == 0:
            self.ui.borrar_ok.setText("NO EXISTE")

        else:
            self.ui.borrar_ok.setText("Consultar")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mi_app = Pedido()
    mi_app.show()
    sys.exit(app.exec_())
