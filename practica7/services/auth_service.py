from enum import Enum
from dataclasses import dataclass

class UserRole(Enum):
    ADMIN = "admin"
    MAESTRO = "maestro"
    ALUMNO = "alumno"

@dataclass(frozen=True)
class User:
    username: str
    role: UserRole
    nombre: str

@dataclass(frozen=True)
class AuthResult:
    ok: bool
    message: str = ""
    user: User = None

class AuthService:
    """
    Servicio de autenticación con tres tipos de usuarios
    """

    def __init__(self):
        
        self._users = {
            "admin": {"password": "admin123", "role": UserRole.ADMIN, "nombre": "Administrador"},
            "juanperez": {"password": "maestro2024", "role": UserRole.MAESTRO, "nombre": "Juan Pérez"},
            "mariagarcia": {"password": "alumno2024", "role": UserRole.ALUMNO, "nombre": "María García"}
        }

    def login(self, username: str, password: str) -> AuthResult:
        if not username or not password:
            return AuthResult(False, "Usuario y contraseña son requeridos.")

        username = username.lower().strip()
        user_data = self._users.get(username)

        if user_data and user_data["password"] == password:
            user = User(
                username=username,
                role=user_data["role"],
                nombre=user_data["nombre"]
            )
            return AuthResult(True, f"Bienvenido {user_data['nombre']}", user)

        return AuthResult(False, "Usuario o contraseña incorrectos")