from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QLabel, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QGroupBox, QListWidget

class AdminView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Panel de Administrador")
        self.resize(600, 400)
        
        
        self.lbl_titulo = QLabel("Panel de Administrador")
        self.lbl_titulo.setAlignment(Qt.AlignCenter)
        self.lbl_titulo.setStyleSheet("font-size: 20px; font-weight: bold; color: #B71C1C;")
        
    
        self.lbl_bienvenida = QLabel()
        self.lbl_bienvenida.setAlignment(Qt.AlignCenter)
        self.lbl_bienvenida.setStyleSheet("font-size: 14px; margin: 10px;")
        
        
        group_usuarios = QGroupBox("Gestión de Usuarios")
        group_usuarios.setStyleSheet("QGroupBox { font-weight: bold; font-size: 14px; }")
        
        self.lista_usuarios = QListWidget()
        self.lista_usuarios.addItems([
            "admin (Administrador)",
            "juanperez (Maestro)",
            "mariagarcia (Alumno)",
            "analopez (Maestro)",
            "carlosruiz (Alumno)"
        ])
        
        self.btn_agregar_usuario = QPushButton("Agregar Usuario")
        self.btn_editar_usuario = QPushButton("Editar Usuario")
        self.btn_eliminar_usuario = QPushButton("Eliminar Usuario")
        
        layout_botones_usuarios = QHBoxLayout()
        layout_botones_usuarios.addWidget(self.btn_agregar_usuario)
        layout_botones_usuarios.addWidget(self.btn_editar_usuario)
        layout_botones_usuarios.addWidget(self.btn_eliminar_usuario)
        
        layout_usuarios = QVBoxLayout()
        layout_usuarios.addWidget(self.lista_usuarios)
        layout_usuarios.addLayout(layout_botones_usuarios)
        group_usuarios.setLayout(layout_usuarios)
        
        
        group_reportes = QGroupBox("Reportes del Sistema")
        group_reportes.setStyleSheet("QGroupBox { font-weight: bold; font-size: 14px; }")
        
        self.btn_reportes_maestros = QPushButton("Reporte de Maestros")
        self.btn_reportes_alumnos = QPushButton("Reporte de Alumnos")
        self.btn_estadisticas = QPushButton("Estadísticas Generales")
        
        layout_reportes = QHBoxLayout()
        layout_reportes.addWidget(self.btn_reportes_maestros)
        layout_reportes.addWidget(self.btn_reportes_alumnos)
        layout_reportes.addWidget(self.btn_estadisticas)
        group_reportes.setLayout(layout_reportes)
        
        
        self.btn_cerrar_sesion = QPushButton("Cerrar Sesión")
        self.btn_cerrar_sesion.setStyleSheet("background-color: #dc3545; color: white;")
        
        
        layout = QVBoxLayout(self)
        layout.addWidget(self.lbl_titulo)
        layout.addWidget(self.lbl_bienvenida)
        layout.addWidget(group_usuarios)
        layout.addWidget(group_reportes)
        layout.addWidget(self.btn_cerrar_sesion)
    
    def set_usuario(self, nombre: str):
        self.lbl_bienvenida.setText(f"Bienvenido, {nombre}")