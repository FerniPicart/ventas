"""
Modelo SQLAlchemy para tabla ventasmovi
TODO: CONFIGURAR MANUALMENTE - Ajustar campos según tu tabla real en SQL Server
Inspecciona tu tabla con: SELECT TOP 1 * FROM ventasmovi
"""

from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.database import Base

class VentaMovi(Base):
    __tablename__ = "ventasmovi"
    
    # TODO: CONFIGURAR MANUALMENTE - Estos son campos genéricos
    # Reemplaza con las columnas reales de tu tabla ventasmovi
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    
    # Ejemplo de campos comunes (ajusta según tu schema real)
    # venta_id = Column(Integer, ForeignKey("ventas.id"))
    # producto = Column(String(255))
    # cantidad = Column(Integer)
    # precio_unitario = Column(Float)
    # subtotal = Column(Float)
    # created_at = Column(DateTime, server_default=func.now())
    
    def __repr__(self):
        return f"<VentaMovi {self.id}>"