from fastapi import APIRouter

from .endpoints import saludo

router = APIRouter()
router.include_router(saludo.router, prefix="/saludo", tags=["Saludo"])
