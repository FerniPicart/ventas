"""
Schemas Pydantic para validación de datos
"""

from app.schemas.user import UserCreate, UserResponse, UserUpdate
from app.schemas.auth import Token, TokenRefresh, LoginRequest, RegisterRequest, ResetPasswordRequest, ResetPassword
from app.schemas.venta import VentaCreate, VentaResponse, VentaUpdate
from app.schemas.venta_movi import VentaMoviCreate, VentaMoviResponse, VentaMoviUpdate
from app.schemas.oportunidad import OportunidadCreate, OportunidadResponse, OportunidadUpdate
from app.schemas.oportu_movi import OportunMoviCreate, OportunMoviResponse, OportunMoviUpdate

__all__ = [
    "UserCreate", "UserResponse", "UserUpdate",
    "Token", "TokenRefresh", "LoginRequest", "RegisterRequest", "ResetPasswordRequest", "ResetPassword",
    "VentaCreate", "VentaResponse", "VentaUpdate",
    "VentaMoviCreate", "VentaMoviResponse", "VentaMoviUpdate",
    "OportunidadCreate", "OportunidadResponse", "OportunidadUpdate",
    "OportunMoviCreate", "OportunMoviResponse", "OportunMoviUpdate",
]