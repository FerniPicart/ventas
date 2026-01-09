"""
Modelo SQLAlchemy para tabla ventas
TODO: CONFIGURAR MANUALMENTE - Ajustar campos según tu tabla real en SQL Server
Inspecciona tu tabla con: SELECT TOP 1 * FROM ventas
"""

from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from sqlalchemy.sql import func
from app.database import Base

class Venta(Base):
    __tablename__ = "ventas"
    
    # TODO: CONFIGURAR MANUALMENTE - Estos son campos genéricos
    # Reemplaza con las columnas reales de tu tabla ventas
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    
    # Ejemplo de campos comunes (ajusta según tu schema real)
    # cliente = Column(String(255))
    # total = Column(Float)
    # fecha = Column(DateTime)
    # estado = Column(String(50))
    # observaciones = Column(Text)
    # created_at = Column(DateTime, server_default=func.now())
    
    def __repr__(self):
        return f"<Venta {self.id}>"