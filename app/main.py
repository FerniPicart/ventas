"""
FastAPI - Aplicación Principal
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

from app.config import settings
from app.routes import auth, ventas, ventasmovi, oportunidades, oportumovi

# Validar configuración al iniciar
settings.validate_config()

# Crear aplicación FastAPI
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="API REST segura con autenticación JWT para gestión de ventas",
    docs_url="/docs",  # Swagger UI
    redoc_url="/redoc",  # ReDoc
)

# ========================================
# Rate Limiting
# ========================================
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# ========================================
# CORS Configuration
# TODO: CONFIGURAR MANUALMENTE - Ajustar según tu frontend
# ========================================
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_URL],  # URL de tu frontend Next.js
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ========================================
# Routes
# ========================================
app.include_router(auth.router, prefix="/auth", tags=["Autenticación"])
app.include_router(ventas.router, prefix="/ventas", tags=["Ventas"])
app.include_router(ventasmovi.router, prefix="/ventasmovi", tags=["Ventas Movimientos"])
app.include_router(oportunidades.router, prefix="/oportunidades", tags=["Oportunidades"])
app.include_router(oportumovi.router, prefix="/oportumovi", tags=["Oportunidades Movimientos"])

# ========================================
# Health Check
# ========================================
@app.get("/health", tags=["Health"])
async def health_check():
    """
    Endpoint para verificar que la API está funcionando
    """
    return {
        "status": "healthy",
        "app": settings.APP_NAME,
        "version": settings.APP_VERSION
    }

@app.get("/", tags=["Root"])
async def root():
    """
    Endpoint raíz - redirige a documentación
    """
    return {
        "message": f"Bienvenido a {settings.APP_NAME}",
        "docs": "/docs",
        "redoc": "/redoc"
    }