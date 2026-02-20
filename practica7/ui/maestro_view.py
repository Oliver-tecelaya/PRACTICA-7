from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QGroupBox, QListWidget

class MaestroView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Panel del Maestro")
        self.resize(600, 400)

        # Título
        self.lbl_titulo = QLabel("Panel del Maestro")
        self.lbl_titulo.setAlignment(Qt.AlignCenter)
        self.lbl_titulo.setStyleSheet("font-size: 20px; font-weight: bold; color: #1565C0;")

        #informacion
        self.lbl_bienvenida = QLabel()
        self.lbl_bienvenida.setAlignment(Qt.AlignCenter)
        self.lbl_bienvenida.setStyleSheet("font-size: 14px; margin: 10px;")

        # Cursos
        group_cursos = QGroupBox("Mis Cursos")
        group_cursos.setStyleSheet("QGroupBox { font-weight: bold; font-size: 14px; }")

        self.lista_cursos = QListWidget()
        self.lista_cursos.addItems([
            "Matemáticas - Grupo A",
            "Matemáticas - Grupo B",
            "Física - Grupo A",
            "Programación - Grupo B"
        ])

        layout_cursos = QVBoxLayout()
        layout_cursos.addWidget(self.lista_cursos)
        group_cursos.setLayout(layout_cursos)

        # Tareas
        group_tareas = QGroupBox("Tareas por Calificar")
        group_tareas.setStyleSheet("QGroupBox { font-weight: bold; font-size: 14px; }")

        self.lista_tareas = QListWidget()
        self.lista_tareas.addItems([
            "Examen Matemáticas - 15 pendientes",
            "Tarea Física - 8 pendientes",
            "Proyecto Programación - 12 pendientes"
        ])

        layout_tareas = QVBoxLayout()
        layout_tareas.addWidget(self.lista_tareas)
        group_tareas.setLayout(layout_tareas)


        self.btn_ver_calificaciones = QPushButton("Ver Calificaciones")
        self.btn_subir_notas = QPushButton("Subir Notas")
        self.btn_cerrar_sesion = QPushButton("Cerrar Sesión")
        self.btn_cerrar_sesion.setStyleSheet("background-color: #dc3545; color: white;")

        layout_botones = QHBoxLayout()
        layout_botones.addWidget(self.btn_ver_calificaciones)
        layout_botones.addWidget(self.btn_subir_notas)
        layout_botones.addWidget(self.btn_cerrar_sesion)


        layout = QVBoxLayout(self)
        layout.addWidget(self.lbl_titulo)
        layout.addWidget(self.lbl_bienvenida)
        layout.addWidget(group_cursos)
        layout.addWidget(group_tareas)
        layout.addLayout(layout_botones)

    def set_usuario(self, nombre: str):
        self.lbl_bienvenida.setText(f"Bienvenido, {nombre}")