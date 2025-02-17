from fastapi import APIRouter

from .endpoints import saludo, todo

router = APIRouter()
router.include_router(saludo.router, prefix="/saludo", tags=["Saludo"])
router.include_router(todo.router, prefix="/todo", tags=["Todo"])
