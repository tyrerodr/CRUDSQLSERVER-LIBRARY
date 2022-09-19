import sys
from VENTANAS.GUIRevista import * 
from DAO.RevistaDAO import *
from PyQt5.QtWidgets import QTableWidgetItem


class Revista(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.datosTotal = Registro_datos()
        self.ui.bt_refrescar.clicked.connect(self.m_productos)
        self.ui.bt_agregar.clicked.connect(self.insert_Revista)
        self.ui.bt_borrar.clicked.connect(self.eliminar_producto)
        self.ui.bt_actualizar.clicked.connect(self.modificar_Revistas)
        self.ui.id_buscar.clicked.connect(self.set_actualizarpage)
        self.ui.borrar_ok.clicked.connect(self.consultar_borrado)

        self.ui.tabla_borrar.setColumnWidth(0, 98)
        self.ui.tabla_borrar.setColumnWidth(1, 100)
        self.ui.tabla_borrar.setColumnWidth(2, 98)
        self.ui.tabla_borrar.setColumnWidth(3, 98)
        self.ui.tabla_borrar.setColumnWidth(4, 98)

        self.ui.tabla_revistas.setColumnWidth(0, 98)
        self.ui.tabla_revistas.setColumnWidth(1, 100)
        self.ui.tabla_revistas.setColumnWidth(2, 98)
        self.ui.tabla_revistas.setColumnWidth(3, 98)
        self.ui.tabla_revistas.setColumnWidth(4, 98)

    def m_productos(self):
        datos = self.datosTotal.buscar_Revista()
        i = len(datos)

        self.ui.tabla_revistas.setRowCount(i)
        tablerow = 0
        for row in datos:
            self.ui.tabla_revistas.setItem(
                tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.ui.tabla_revistas.setItem(
                tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.ui.tabla_revistas.setItem(
                tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            tablerow += 1

    def insert_Revista(self):
        idA = self.ui.idA.text()
        tipoA = self.ui.tipoA.text()
        contador_revistaA = self.ui.contador_revistaA.text()

        self.datosTotal.inserta_Revista(
            idA, tipoA, contador_revistaA)

        self.ui.idA.clear()
        self.ui.tipoA.clear()
        self.ui.contador_revistaA.clear()


    def set_actualizarpage(self):
        id_revista = self.ui.id_revista.text()
        id_revista = str("'" + id_revista + "'")
        nombreXX = self.datosTotal.busca_Revista(id_revista)
        print(nombreXX)

        if nombreXX != []:
            print(self.datosTotal.busca_Revista(id_revista))
            datos = self.datosTotal.busca_Revista(id_revista)[0]
            print(datos[0])
            self.ui.id_actualizar.setText(str(datos[0]))
            self.ui.tipo_actualizar.setText(str(datos[1]))
            self.ui.contador_revista_actualizar.setText(str(datos[2]))


    def modificar_Revistas(self):
        id_revista = self.ui.id_revista.text()
        id_revista = str("'" + id_revista + "'")
        nombreXX = self.datosTotal.busca_Revista(id_revista)

        if nombreXX != None:
            self.ui.id_buscar.setText("ACTUALIZAR")
            idM = self.ui.id_actualizar.text()
            tipoM = self.ui.tipo_actualizar.text()
            contador_revistaM = self.ui.contador_revista_actualizar.text()


            act = self.datosTotal.actualiza_Revista(
                idM, tipoM, contador_revistaM)
            if act == 1:
                self.ui.id_buscar.setText("ACTUALIZADO")
                self.ui.id_actualizar.clear()
                self.ui.tipo_actualizar.clear()
                self.ui.contador_revista_actualizar.clear()
                
                self.ui.id_revista.clear()

            elif act == 0:
                self.ui.id_buscar.setText("ERROR")
            else:
                self.ui.id_buscar.setText("INCORRECTO")
        else:
            self.ui.id_buscar.setText("NO EXISTE")


    def consultar_borrado(self):
        datos = self.datosTotal.buscar_Revista()
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
        resp = (self.datosTotal.elimina_Revista(eliminar))
        if resp == None:
            self.ui.borrar_ok.setText("NO EXISTE")
        elif resp == 0:
            self.ui.borrar_ok.setText("NO EXISTE")

        else:
            self.ui.borrar_ok.setText("Consultar")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mi_app = Revista()
    mi_app.show()
    sys.exit(app.exec_())
