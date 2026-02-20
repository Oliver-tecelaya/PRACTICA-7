from PyQt5.QtWidgets import QStackedWidget
from ui.login_view import LoginView
from ui.admin_view import AdminView
from ui.maestro_view import MaestroView
from ui.alumno_view import AlumnoView
from services.auth_service import AuthService, UserRole
from presenters.login_presenter import LoginPresenter

class AppShell(QStackedWidget):
    PAGE_LOGIN = 0
    PAGE_ADMIN = 1
    PAGE_MAESTRO = 2
    PAGE_ALUMNO = 3

    def __init__(self):
        super().__init__()

        self.login_view = LoginView()
        self.admin_view = AdminView()
        self.maestro_view = MaestroView()
        self.alumno_view = AlumnoView()

        self.auth_service = AuthService()

        self.login_presenter = LoginPresenter(
            view=self.login_view,
            auth=self.auth_service,
            on_success=self._go_to_role_view
        )

        self.addWidget(self.login_view)  
        self.addWidget(self.admin_view)  
        self.addWidget(self.maestro_view)  
        self.addWidget(self.alumno_view)  

        self.setCurrentIndex(self.PAGE_LOGIN)
        self.setWindowTitle("Sistema Educativo - MVP")
        self.resize(640, 480)

        
        self.admin_view.btn_cerrar_sesion.clicked.connect(self._logout)
        self.maestro_view.btn_cerrar_sesion.clicked.connect(self._logout)
        self.alumno_view.btn_cerrar_sesion.clicked.connect(self._logout)

    def _go_to_role_view(self, user):
        """Navega a la vista correspondiente según el rol del usuario"""
        if user.role == UserRole.ADMIN:
            self.admin_view.set_usuario(user.nombre)
            self.setCurrentIndex(self.PAGE_ADMIN)
        elif user.role == UserRole.MAESTRO:
            self.maestro_view.set_usuario(user.nombre)
            self.setCurrentIndex(self.PAGE_MAESTRO)
        elif user.role == UserRole.ALUMNO:
            self.alumno_view.set_usuario(user.nombre)
            self.setCurrentIndex(self.PAGE_ALUMNO)

    def _logout(self):
        self.login_view.clear_password()
        self.login_view.txt_usuario.clear()
        self.setCurrentIndex(self.PAGE_LOGIN)