# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUIPedido.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(745, 400)
        Form.setMinimumSize(QtCore.QSize(681, 400))
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.pantalla = QtWidgets.QTabWidget(Form)
        self.pantalla.setEnabled(True)
        self.pantalla.setGeometry(QtCore.QRect(0, 0, 751, 400))
        self.pantalla.setMinimumSize(QtCore.QSize(681, 400))
        self.pantalla.setStyleSheet("background-color: rgb(223, 223, 223);\n"
"selection-color: rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);\n"
"selection-background-color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(255, 255, 255);")
        self.pantalla.setObjectName("pantalla")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tabla_pedidos = QtWidgets.QTableWidget(self.tab_5)
        self.tabla_pedidos.setRowCount(0)
        self.tabla_pedidos.setColumnCount(7)
        self.tabla_pedidos.setObjectName("tabla_pedidos")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 0, 191))
        self.tabla_pedidos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(85, 255, 127))
        self.tabla_pedidos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 248, 53))
        self.tabla_pedidos.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(0, 170, 127))
        self.tabla_pedidos.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 170, 0))
        self.tabla_pedidos.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(0, 85, 255))
        self.tabla_pedidos.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(170, 85, 127))
        self.tabla_pedidos.setHorizontalHeaderItem(6, item)
        self.horizontalLayout_3.addWidget(self.tabla_pedidos)
        self.bt_refrescar = QtWidgets.QPushButton(self.tab_5)
        self.bt_refrescar.setStyleSheet("background-color: rgb(85, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.bt_refrescar.setObjectName("bt_refrescar")
        self.horizontalLayout_3.addWidget(self.bt_refrescar)
        self.pantalla.addTab(self.tab_5, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.bt_agregar = QtWidgets.QPushButton(self.tab_2)
        self.bt_agregar.setGeometry(QtCore.QRect(310, 290, 75, 23))
        self.bt_agregar.setStyleSheet("background-color: rgb(85, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.bt_agregar.setObjectName("bt_agregar")
        self.layoutWidget = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 50, 241, 211))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.idA = QtWidgets.QLineEdit(self.layoutWidget)
        self.idA.setObjectName("idA")
        self.verticalLayout.addWidget(self.idA)
        self.solicitanteA = QtWidgets.QLineEdit(self.layoutWidget)
        self.solicitanteA.setObjectName("solicitanteA")
        self.verticalLayout.addWidget(self.solicitanteA)
        self.lista_materialA = QtWidgets.QLineEdit(self.layoutWidget)
        self.lista_materialA.setObjectName("lista_materialA")
        self.verticalLayout.addWidget(self.lista_materialA)
        self.materiaA = QtWidgets.QLineEdit(self.layoutWidget)
        self.materiaA.setObjectName("materiaA")
        self.verticalLayout.addWidget(self.materiaA)
        self.fecha_prestamoA = QtWidgets.QLineEdit(self.layoutWidget)
        self.fecha_prestamoA.setObjectName("fecha_prestamoA")
        self.verticalLayout.addWidget(self.fecha_prestamoA)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.layoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget_2.setGeometry(QtCore.QRect(380, 50, 231, 211))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_14 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_5.addWidget(self.label_14)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_5.addWidget(self.label_15)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.fecha_devolucionA = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.fecha_devolucionA.setObjectName("fecha_devolucionA")
        self.verticalLayout_6.addWidget(self.fecha_devolucionA)
        self.contador_pedidoA = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.contador_pedidoA.setObjectName("contador_pedidoA")
        self.verticalLayout_6.addWidget(self.contador_pedidoA)
        self.horizontalLayout_4.addLayout(self.verticalLayout_6)
        self.pantalla.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.bt_actualizar = QtWidgets.QPushButton(self.tab_3)
        self.bt_actualizar.setGeometry(QtCore.QRect(440, 290, 91, 21))
        self.bt_actualizar.setStyleSheet("background-color: rgb(85, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.bt_actualizar.setObjectName("bt_actualizar")
        self.id_pedido = QtWidgets.QLineEdit(self.tab_3)
        self.id_pedido.setGeometry(QtCore.QRect(30, 120, 180, 20))
        self.id_pedido.setObjectName("id_pedido")
        self.label_13 = QtWidgets.QLabel(self.tab_3)
        self.label_13.setGeometry(QtCore.QRect(30, 70, 191, 39))
        self.label_13.setObjectName("label_13")
        self.id_buscar = QtWidgets.QPushButton(self.tab_3)
        self.id_buscar.setGeometry(QtCore.QRect(70, 150, 75, 23))
        self.id_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.id_buscar.setObjectName("id_buscar")
        self.layoutWidget_3 = QtWidgets.QWidget(self.tab_3)
        self.layoutWidget_3.setGeometry(QtCore.QRect(240, 40, 241, 211))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_3.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_3.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_3.addWidget(self.label_11)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.id_actualizar = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.id_actualizar.setObjectName("id_actualizar")
        self.verticalLayout_4.addWidget(self.id_actualizar)
        self.solicitante_actualizar = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.solicitante_actualizar.setObjectName("solicitante_actualizar")
        self.verticalLayout_4.addWidget(self.solicitante_actualizar)
        self.lista_material_actualizar = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lista_material_actualizar.setObjectName("lista_material_actualizar")
        self.verticalLayout_4.addWidget(self.lista_material_actualizar)
        self.materia_actualizar = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.materia_actualizar.setObjectName("materia_actualizar")
        self.verticalLayout_4.addWidget(self.materia_actualizar)
        self.fecha_prestamo_actualizar = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.fecha_prestamo_actualizar.setObjectName("fecha_prestamo_actualizar")
        self.verticalLayout_4.addWidget(self.fecha_prestamo_actualizar)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.layoutWidget_4 = QtWidgets.QWidget(self.tab_3)
        self.layoutWidget_4.setGeometry(QtCore.QRect(490, 40, 231, 211))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_16 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_7.addWidget(self.label_16)
        self.label_17 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_7.addWidget(self.label_17)
        self.horizontalLayout_5.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.fecha_devolucion_actualizar = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.fecha_devolucion_actualizar.setObjectName("fecha_devolucion_actualizar")
        self.verticalLayout_8.addWidget(self.fecha_devolucion_actualizar)
        self.contador_pedido_actualizar = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.contador_pedido_actualizar.setObjectName("contador_pedido_actualizar")
        self.verticalLayout_8.addWidget(self.contador_pedido_actualizar)
        self.horizontalLayout_5.addLayout(self.verticalLayout_8)
        self.pantalla.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.cedula_borrar = QtWidgets.QLineEdit(self.tab_4)
        self.cedula_borrar.setGeometry(QtCore.QRect(271, 40, 101, 20))
        self.cedula_borrar.setText("")
        self.cedula_borrar.setObjectName("cedula_borrar")
        self.label_12 = QtWidgets.QLabel(self.tab_4)
        self.label_12.setGeometry(QtCore.QRect(220, 40, 45, 16))
        self.label_12.setObjectName("label_12")
        self.borrar_ok = QtWidgets.QPushButton(self.tab_4)
        self.borrar_ok.setGeometry(QtCore.QRect(630, 210, 91, 23))
        self.borrar_ok.setStyleSheet("background-color: rgb(255, 0, 127);")
        self.borrar_ok.setObjectName("borrar_ok")
        self.bt_borrar = QtWidgets.QPushButton(self.tab_4)
        self.bt_borrar.setGeometry(QtCore.QRect(390, 40, 75, 23))
        self.bt_borrar.setStyleSheet("background-color: rgb(85, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.bt_borrar.setObjectName("bt_borrar")
        self.tabla_borrar = QtWidgets.QTableWidget(self.tab_4)
        self.tabla_borrar.setGeometry(QtCore.QRect(10, 90, 591, 251))
        self.tabla_borrar.setRowCount(0)
        self.tabla_borrar.setColumnCount(7)
        self.tabla_borrar.setObjectName("tabla_borrar")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 0, 191))
        self.tabla_borrar.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(85, 255, 127))
        self.tabla_borrar.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 248, 53))
        self.tabla_borrar.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(0, 170, 127))
        self.tabla_borrar.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 170, 0))
        self.tabla_borrar.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(0, 85, 255))
        self.tabla_borrar.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(170, 85, 127))
        self.tabla_borrar.setHorizontalHeaderItem(6, item)
        self.pantalla.addTab(self.tab_4, "")

        self.retranslateUi(Form)
        self.pantalla.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "REGISTRO DE PEDIDOS"))
        item = self.tabla_pedidos.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Id"))
        item = self.tabla_pedidos.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Solicitante"))
        item = self.tabla_pedidos.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Lista Material"))
        item = self.tabla_pedidos.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Materia"))
        item = self.tabla_pedidos.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Fecha Prestamo"))
        item = self.tabla_pedidos.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Fecha Devolucion"))
        item = self.tabla_pedidos.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Contador Pedidos"))
        self.bt_refrescar.setText(_translate("Form", "REFRESCAR"))
        self.pantalla.setTabText(self.pantalla.indexOf(self.tab_5), _translate("Form", "PEDIDOS"))
        self.bt_agregar.setText(_translate("Form", "AGREGAR"))
        self.label_2.setText(_translate("Form", "ID:"))
        self.label_3.setText(_translate("Form", "SOLICITANTE:"))
        self.label_4.setText(_translate("Form", "LISTA MATERIAL"))
        self.label_5.setText(_translate("Form", "MATERIA"))
        self.label_6.setText(_translate("Form", "FECHA PRESTAMO"))
        self.label_14.setText(_translate("Form", "FECHA DEVOLUCIÓN"))
        self.label_15.setText(_translate("Form", "CONTADOR PEDIDO"))
        self.pantalla.setTabText(self.pantalla.indexOf(self.tab_2), _translate("Form", "AGREGAR NUEVOS PEDIDOS"))
        self.bt_actualizar.setText(_translate("Form", "ACTUALIZAR"))
        self.label_13.setText(_translate("Form", "INGRESE EL ID DEL PEDIDO"))
        self.id_buscar.setText(_translate("Form", "BUSCAR"))
        self.label_7.setText(_translate("Form", "ID:"))
        self.label_8.setText(_translate("Form", "SOLICITANTE:"))
        self.label_9.setText(_translate("Form", "LISTA MATERIAL"))
        self.label_10.setText(_translate("Form", "MATERIA"))
        self.label_11.setText(_translate("Form", "FECHA PRESTAMO"))
        self.label_16.setText(_translate("Form", "FECHA DEVOLUCIÓN"))
        self.label_17.setText(_translate("Form", "CONTADOR PEDIDO"))
        self.pantalla.setTabText(self.pantalla.indexOf(self.tab_3), _translate("Form", "ACTUALIZAR PEDIDOS"))
        self.label_12.setText(_translate("Form", "ID:"))
        self.borrar_ok.setText(_translate("Form", "Consultar"))
        self.bt_borrar.setText(_translate("Form", "BORRAR"))
        item = self.tabla_borrar.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Id"))
        item = self.tabla_borrar.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Solicitante"))
        item = self.tabla_borrar.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Lista Material"))
        item = self.tabla_borrar.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Materia"))
        item = self.tabla_borrar.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Fecha Prestamo"))
        item = self.tabla_borrar.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Fecha Devolucion"))
        item = self.tabla_borrar.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Contador Pedidos"))
        self.pantalla.setTabText(self.pantalla.indexOf(self.tab_4), _translate("Form", "BORRAR PEDIDOS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
