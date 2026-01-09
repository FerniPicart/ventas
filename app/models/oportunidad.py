"""
Modelo SQLAlchemy para tabla oportunidades
TODO: CONFIGURAR MANUALMENTE - Ajustar campos según tu tabla real en SQL Server
Inspecciona tu tabla con: SELECT TOP 1 * FROM oportunidades
"""

from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from sqlalchemy.sql import func
from app.database import Base

class Oportunidad(Base):
    __tablename__ = "oportunidades"
    
    # TODO: CONFIGURAR MANUALMENTE - Estos son campos genéricos
    # Reemplaza con las columnas reales de tu tabla oportunidades
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    
    # Ejemplo de campos comunes (ajusta según tu schema real)
    # cliente = Column(String(255))
    # monto_estimado = Column(Float)
    # probabilidad = Column(Integer)
    # estado = Column(String(50))
    # fecha_cierre_estimada = Column(DateTime)
    # observaciones = Column(Text)
    # created_at = Column(DateTime, server_default=func.now())
    
    def __repr__(self):
        return f"<Oportunidad {self.id}>"