"""
Schemas Pydantic para Venta
TODO: CONFIGURAR MANUALMENTE - Ajustar según tu modelo real
"""

from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class VentaBase(BaseModel):
    # TODO: CONFIGURAR MANUALMENTE - Añade los campos reales de tu tabla ventas
    pass

class VentaCreate(VentaBase):
    pass

class VentaUpdate(BaseModel):
    # TODO: CONFIGURAR MANUALMENTE - Campos opcionales para actualizar
    pass

class VentaResponse(VentaBase):
    id: int
    
    class Config:
        from_attributes = True