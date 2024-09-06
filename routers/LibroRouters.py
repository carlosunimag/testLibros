from fastapi import APIRouter
from typing import Any
from pydantic import BaseModel, Field

from controllers.LibroController import LibroController

class LibroBM(BaseModel):
    id: int = None
    title: str = Field(default='Titulo del libro', min_length=5, max_length=40)
    autor: str = Field(default='Autor del libro', min_length=5, max_length=20)
    disponible: bool = None


routerLibro = APIRouter(prefix='/libro')

@routerLibro.get('/', tags=['Libros'])
def get_all_libros():
    return LibroController.getAllLibros()

@routerLibro.get('/{id}', tags=['Libros'])
def get_libro(id: int):
    return LibroController.getLibroById(id)

@routerLibro.post('/create/',tags=['Libros'])
def post_create_libro(libro: LibroBM):
    return LibroController.createLibro(libro)
