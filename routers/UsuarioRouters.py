from fastapi import APIRouter
from typing import Any
from pydantic import BaseModel, Field

from controllers.UsuarioController import UsuarioController

class UsuarioBM(BaseModel):
    id:int
    nombre: str = Field(default='Nombre del usuario', min_length=5, max_length=40)
    libros_prestados: str = Field(default='[]')

routerUsuario = APIRouter(prefix='/usuario')

@routerUsuario.post('/prestar_libro/{usario_id}/{libro_id}', tags=['Usuario'])
def post_prestar_book(usuario_id: int, libro_id: int):
    return UsuarioController.prestarLibro(usuario_id,libro_id)

@routerUsuario.post('/devolver_libro/{usario_id}/{libro_id}', tags=['Usuario'])
def post_devolver_book(usuario_id: int, libro_id: int):
    return UsuarioController.devolverLibro(usuario_id,libro_id)

@routerUsuario.post('/create/', tags=['Usuario'])
def post_create_usuario(usuario: UsuarioBM):
    return UsuarioController.createUsuario(usuario)
