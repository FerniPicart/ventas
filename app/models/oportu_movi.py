"""
Modelo SQLAlchemy para tabla oportumovi
TODO: CONFIGURAR MANUALMENTE - Ajustar campos según tu tabla real en SQL Server
Inspecciona tu tabla con: SELECT TOP 1 * FROM oportumovi
"""

from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.sql import func
from app.database import Base

class OportunMovi(Base):
    __tablename__ = "oportumovi"
    
    # TODO: CONFIGURAR MANUALMENTE - Estos son campos genéricos
    # Reemplaza con las columnas reales de tu tabla oportumovi
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    
    # Ejemplo de campos comunes (ajusta según tu schema real)
    # oportunidad_id = Column(Integer, ForeignKey("oportunidades.id"))
    # accion = Column(String(255))
    # descripcion = Column(Text)
    # fecha = Column(DateTime)
    # created_at = Column(DateTime, server_default=func.now())
    
    def __repr__(self):
        return f"<OportunMovi {self.id}>"