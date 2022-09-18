import sys
from BIBLIOTECA.Docente import Docente
from BIBLIOTECA.Revista import Revista
from BIBLIOTECA.Persona import Persona
from BIBLIOTECA.Material import Material
from BIBLIOTECA.Pedido import Pedido
from BIBLIOTECA.Libro import Libro
from BIBLIOTECA.Estudiante import Estudiante
from GUIBiblioteca import *
from PyQt5.QtWidgets import QTableWidgetItem


class Biblioteca(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.btn_estudiantes.clicked.connect(self.abrirEstudiante)
        self.ui.btn_libros.clicked.connect(self.abrirLibro)
        self.ui.btn_pedidos.clicked.connect(self.abrirPedido)
        self.ui.btn_materiales.clicked.connect(self.abrirMaterial)
        self.ui.btn_personas.clicked.connect(self.abrirPersona)
        self.ui.btn_revistas.clicked.connect(self.abrirRevista)
        self.ui.btn_docentes.clicked.connect(self.abrirDocente)
    
    def abrirDocente(self):
        self.ui = Docente()
        self.ui.show()
    
    def abrirRevista(self):
        self.ui = Revista()
        self.ui.show()
    
    
    def abrirPersona(self):
        self.ui = Persona()
        self.ui.show()
    
    
    def abrirMaterial(self):
        self.ui = Material()
        self.ui.show()
    
    
    def abrirPedido(self):
        self.ui = Pedido()
        self.ui.show()
    
    
    def abrirLibro(self):
        self.ui = Libro()
        self.ui.show()
    
    def abrirEstudiante(self):
        self.ui = Estudiante()
        self.ui.show()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mi_app = Biblioteca()
    mi_app.show()
    sys.exit(app.exec_())
