from fastapi import APIRouter
from typing import Any
from pydantic import BaseModel, Field

from routers.LibroRouters import LibroBM
from routers.UsuarioRouters import UsuarioBM
from controllers.LibroController import LibroController
from controllers.UsuarioController import UsuarioController

class Biblioteca(BaseModel):
    id:int
    libros: list
    usuarios: list

routerBiblioteca = APIRouter(prefix='/biblioteca')

@routerBiblioteca.post('/agregar_libro/', tags=['Biblioteca'])
def post_prestar_book(libro: LibroBM):
    return LibroController.createLibro(libro)

@routerBiblioteca.post('/registrar_usuario/', tags=['Biblioteca'])
def post_create_usuario(usuario: UsuarioBM):
    return UsuarioController.createUsuario(usuario)

@routerBiblioteca.post('/prestar_libro/{usario_id}/{titulo_libro}', tags=['Biblioteca'])
def post_prestar_book(usuario_id: int, titulo_libro: str):
    return UsuarioController.prestarLibroByTitulo(titulo=titulo_libro,usuario_id=usuario_id)

@routerBiblioteca.post('/devolver_libro/{usario_id}/{titulo_libro}', tags=['Biblioteca'])
def post_prestar_book(usuario_id: int, titulo_libro: str):
    return UsuarioController.devolverLibroByTitulo(titulo=titulo_libro,usuario_id=usuario_id)