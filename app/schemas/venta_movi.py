"""
Schemas Pydantic para VentaMovi
TODO: CONFIGURAR MANUALMENTE - Ajustar según tu modelo real
"""

from pydantic import BaseModel
from typing import Optional

class VentaMoviBase(BaseModel):
    # TODO: CONFIGURAR MANUALMENTE - Añade los campos reales de tu tabla ventasmovi
    pass

class VentaMoviCreate(VentaMoviBase):
    pass

class VentaMoviUpdate(BaseModel):
    # TODO: CONFIGURAR MANUALMENTE - Campos opcionales para actualizar
    pass

class VentaMoviResponse(VentaMoviBase):
    id: int
    
    class Config:
        from_attributes = True