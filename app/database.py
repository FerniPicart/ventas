"""
Configuración de la base de datos SQL Server
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings

# TODO: CONFIGURAR MANUALMENTE - Asegúrate de que el .env tenga las credenciales correctas

# Crear engine de SQLAlchemy para SQL Server
engine = create_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG,  # Log de queries SQL en modo debug
    pool_pre_ping=True,  # Verificar conexión antes de usar
)

# Crear SessionLocal para transacciones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para modelos
Base = declarative_base()

# Dependency para obtener sesión de DB
def get_db():
    """
    Dependency que proporciona una sesión de base de datos
    Se cierra automáticamente después de la request
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()