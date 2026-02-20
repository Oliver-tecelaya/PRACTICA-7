from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QGroupBox, QListWidget, QTableWidget, QTableWidgetItem

class AlumnoView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Panel del Alumno")
        self.resize(600, 400)

        
        self.lbl_titulo = QLabel("Panel del Alumno")
        self.lbl_titulo.setAlignment(Qt.AlignCenter)
        self.lbl_titulo.setStyleSheet("font-size: 20px; font-weight: bold; color: #2E7D32;")

        
        self.lbl_bienvenida = QLabel()
        self.lbl_bienvenida.setAlignment(Qt.AlignCenter)
        self.lbl_bienvenida.setStyleSheet("font-size: 14px; margin: 10px;")

        
        group_materias = QGroupBox("Mis Materias")
        group_materias.setStyleSheet("QGroupBox { font-weight: bold; font-size: 14px; }")

        self.lista_materias = QListWidget()
        self.lista_materias.addItems([
            "Matemáticas - Prof. Juan Pérez",
            "Física - Prof. Juan Pérez",
            "Programación - Prof. Ana López",
            "Inglés - Prof. Carlos Ruiz"
        ])

        layout_materias = QVBoxLayout()
        layout_materias.addWidget(self.lista_materias)
        group_materias.setLayout(layout_materias)

        
        group_calificaciones = QGroupBox("Mis Calificaciones")
        group_calificaciones.setStyleSheet("QGroupBox { font-weight: bold; font-size: 14px; }")

        self.tabla_calificaciones = QTableWidget(4, 2)
        self.tabla_calificaciones.setHorizontalHeaderLabels(["Materia", "Calificación"])
        self.tabla_calificaciones.setItem(0, 0, QTableWidgetItem("Matemáticas"))
        self.tabla_calificaciones.setItem(0, 1, QTableWidgetItem("85"))
        self.tabla_calificaciones.setItem(1, 0, QTableWidgetItem("Física"))
        self.tabla_calificaciones.setItem(1, 1, QTableWidgetItem("92"))
        self.tabla_calificaciones.setItem(2, 0, QTableWidgetItem("Programación"))
        self.tabla_calificaciones.setItem(2, 1, QTableWidgetItem("78"))
        self.tabla_calificaciones.setItem(3, 0, QTableWidgetItem("Inglés"))
        self.tabla_calificaciones.setItem(3, 1, QTableWidgetItem("95"))

        layout_calificaciones = QVBoxLayout()
        layout_calificaciones.addWidget(self.tabla_calificaciones)
        group_calificaciones.setLayout(layout_calificaciones)

        
        self.btn_ver_tareas = QPushButton("Ver Tareas Pendientes")
        self.btn_ver_horario = QPushButton("Ver Horario")
        self.btn_cerrar_sesion = QPushButton("Cerrar Sesión")
        self.btn_cerrar_sesion.setStyleSheet("background-color: #dc3545; color: white;")

        layout_botones = QHBoxLayout()
        layout_botones.addWidget(self.btn_ver_tareas)
        layout_botones.addWidget(self.btn_ver_horario)
        layout_botones.addWidget(self.btn_cerrar_sesion)

        
        layout = QVBoxLayout(self)
        layout.addWidget(self.lbl_titulo)
        layout.addWidget(self.lbl_bienvenida)
        layout.addWidget(group_materias)
        layout.addWidget(group_calificaciones)
        layout.addLayout(layout_botones)

    def set_usuario(self, nombre: str):
        self.lbl_bienvenida.setText(f"Bienvenido, {nombre}")