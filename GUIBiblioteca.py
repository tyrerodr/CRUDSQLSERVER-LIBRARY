# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUIBiblioteca.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 419)
        Form.setStyleSheet("background-color: rgb(223, 223, 223);\n"
"selection-color: rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);\n"
"selection-background-color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(255, 255, 255);")
        self.btn_revistas = QtWidgets.QPushButton(Form)
        self.btn_revistas.setGeometry(QtCore.QRect(150, 300, 111, 91))
        self.btn_revistas.setObjectName("btn_revistas")
        self.btn_pedidos = QtWidgets.QPushButton(Form)
        self.btn_pedidos.setGeometry(QtCore.QRect(280, 80, 111, 91))
        self.btn_pedidos.setObjectName("btn_pedidos")
        self.btn_libros = QtWidgets.QPushButton(Form)
        self.btn_libros.setGeometry(QtCore.QRect(280, 190, 111, 91))
        self.btn_libros.setObjectName("btn_libros")
        self.btn_docentes = QtWidgets.QPushButton(Form)
        self.btn_docentes.setGeometry(QtCore.QRect(150, 190, 111, 91))
        self.btn_docentes.setObjectName("btn_docentes")
        self.btn_estudiantes = QtWidgets.QPushButton(Form)
        self.btn_estudiantes.setGeometry(QtCore.QRect(20, 190, 111, 91))
        self.btn_estudiantes.setObjectName("btn_estudiantes")
        self.btn_materiales = QtWidgets.QPushButton(Form)
        self.btn_materiales.setGeometry(QtCore.QRect(150, 80, 111, 91))
        self.btn_materiales.setObjectName("btn_materiales")
        self.btn_personas = QtWidgets.QPushButton(Form)
        self.btn_personas.setGeometry(QtCore.QRect(20, 80, 111, 91))
        self.btn_personas.setObjectName("btn_personas")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(70, 30, 281, 16))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_revistas.setText(_translate("Form", "Revistas"))
        self.btn_pedidos.setText(_translate("Form", "Pedidos"))
        self.btn_libros.setText(_translate("Form", "Libros"))
        self.btn_docentes.setText(_translate("Form", "Docentes"))
        self.btn_estudiantes.setText(_translate("Form", "Estudiantes"))
        self.btn_materiales.setText(_translate("Form", "Materiales"))
        self.btn_personas.setText(_translate("Form", "Personas"))
        self.label.setText(_translate("Form", "BIENVENIDO A LA BIBLIOTECA DE UG"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

