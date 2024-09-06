from fastapi import FastAPI

from BD.database import engine, Base
from routers.LibroRouters import routerLibro
from routers.UsuarioRouters import routerUsuario
from routers.BibliotecaRouters import routerBiblioteca

app = FastAPI(
    title = 'Prueba ',
    version= '0.0.1'
)

aBooks = []
aUsers = []

app.include_router(routerLibro)
app.include_router(routerUsuario)
app.include_router(routerBiblioteca)

Base.metadata.create_all(bind=engine)

@app.get('/')
def index():
    return 'Hola'

