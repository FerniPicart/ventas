"""
Configuración de la aplicación
Carga variables de entorno desde .env
"""

import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

class Settings:
    # ========================================
    # SQL Server Configuration
    # TODO: CONFIGURAR MANUALMENTE en archivo .env
    # ========================================
    DB_SERVER: str = os.getenv("DB_SERVER", "localhost")
    DB_PORT: str = os.getenv("DB_PORT", "1433")
    DB_NAME: str = os.getenv("DB_NAME", "FepasaPr")
    DB_USER: str = os.getenv("DB_USER")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    DB_DRIVER: str = os.getenv("DB_DRIVER", "ODBC Driver 17 for SQL Server")
    
    # Construir connection string para SQL Server
    @property
    def DATABASE_URL(self) -> str:
        return (
            f"mssql+pyodbc://{self.DB_USER}:{self.DB_PASSWORD}@"
            f"{self.DB_SERVER}:{self.DB_PORT}/{self.DB_NAME}"
            f"?driver={self.DB_DRIVER.replace(' ', '+')}"
        )
    
    # ========================================
    # JWT Security
    # TODO: CONFIGURAR MANUALMENTE en archivo .env
    # Genera SECRET_KEY con: python -c "import secrets; print(secrets.token_urlsafe(32))"
    # ========================================
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "180"))
    REFRESH_TOKEN_EXPIRE_DAYS: int = int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS", "7"))
    
    # ========================================
    # App Configuration
    # ========================================
    APP_NAME: str = os.getenv("APP_NAME", "Ventas API")
    APP_VERSION: str = os.getenv("APP_VERSION", "1.0.0")
    DEBUG: bool = os.getenv("DEBUG", "True") == "True"
    
    # ========================================
    # CORS
    # TODO: CONFIGURAR MANUALMENTE en archivo .env
    # ========================================
    FRONTEND_URL: str = os.getenv("FRONTEND_URL", "http://localhost:3000")
    
    # ========================================
    # Email Configuration (para reset de password)
    # TODO: CONFIGURAR DESPUÉS
    # ========================================
    SMTP_HOST: str = os.getenv("SMTP_HOST", "smtp.gmail.com")
    SMTP_PORT: int = int(os.getenv("SMTP_PORT", "587"))
    SMTP_USER: str = os.getenv("SMTP_USER")
    SMTP_PASSWORD: str = os.getenv("SMTP_PASSWORD")
    SMTP_FROM: str = os.getenv("SMTP_FROM")
    
    def validate_config(self):
        """Validar que las configuraciones críticas estén presentes"""
        if not self.SECRET_KEY or self.SECRET_KEY == "CAMBIAR_POR_CLAVE_SUPER_SEGURA_MINIMO_32_CARACTERES":
            raise ValueError("⚠️ SECRET_KEY no configurada. Genera una con: python -c 'import secrets; print(secrets.token_urlsafe(32))'")
        
        if not self.DB_USER or not self.DB_PASSWORD:
            raise ValueError("⚠️ Credenciales de SQL Server no configuradas en .env")

settings = Settings()