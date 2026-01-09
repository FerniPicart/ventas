"""
Schemas Pydantic para Oportunidad
TODO: CONFIGURAR MANUALMENTE - Ajustar según tu modelo real
"""

from pydantic import BaseModel
from typing import Optional

class OportunidadBase(BaseModel):
    # TODO: CONFIGURAR MANUALMENTE - Añade los campos reales de tu tabla oportunidades
    pass

class OportunidadCreate(OportunidadBase):
    pass

class OportunidadUpdate(BaseModel):
    # TODO: CONFIGURAR MANUALMENTE - Campos opcionales para actualizar
    pass

class OportunidadResponse(OportunidadBase):
    id: int
    
    class Config:
        from_attributes = True