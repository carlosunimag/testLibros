from fastapi.responses import JSONResponse
import os
import json

from BD.database import Session
from models.LibroBD import LibroBD
from models.UsuarioBD import UsuarioBD
from helpers.UsuarioHelper import UsuarioHelper
from helpers.LibroHelper import LibroHelper

class UsuarioController:
    
    

    def createUsuario(usuario):
        TEST = bool(os.getenv("TEST", "False"))
        if not TEST:
            us = UsuarioBD(**usuario.model_dump())
            db = Session()
            db.add(us)
            db.commit()
            db.close()
        else:
            USERS =[]
            USERS.append(usuario.__dict__)
            os.environ["USERS"] = json.dumps(USERS)
        return usuario
    
    def prestarLibro(usuario_id, libro_id):
        TEST = bool(os.getenv("TEST", "False"))
        sw = 0
        if not TEST:
            db = Session()

            dataLibro = LibroHelper.validateLibro(db,libro_id)
            if not dataLibro:
                return JSONResponse(status_code=404, content={
                    'message': 'Libro no encontrado'
                })
            
            dataUsuario = UsuarioHelper.validarUsuario(db,usuario_id)
            if not dataUsuario:
                return JSONResponse(status_code=404, content={
                    'message': 'Usuario no encontrado'
                })

            if dataLibro.prestar():
                if dataUsuario.prestar_libro(dataLibro):
                    db.commit()
                    sw = 1
            db.close()
        else:
            BOOKS = json.loads(os.getenv("BOOKS", "[]"))
            USERS = json.loads(os.getenv("USERS", "[]"))
            usuario = UsuarioBD(**USERS[0])
            libro = LibroBD(**BOOKS[0])
            libro.prestar()
            usuario.prestar_libro(libro)
            sw = 1

        if sw:
            return JSONResponse(content={
                'message': 'Libro Prestado'
            })
        
        return JSONResponse(content={
                'message': 'Libro no disponible'
            })
    
    def prestarLibroByTitulo(titulo, usuario_id):
        db = Session()
        dataLibro = LibroHelper.validateLibroByTitulo(db,titulo)

        if not dataLibro:
            return JSONResponse(status_code=404, content={
                'message': 'Libro no encontrado'
            })
        
        dataUsuario = UsuarioHelper.validarUsuario(db,usuario_id)

        if not dataUsuario:
            return JSONResponse(status_code=404, content={
                'message': 'Usuario no encontrado'
            })

        if dataLibro.prestar():
            if dataUsuario.prestar_libro(dataLibro):
                db.commit()
                sw = 1
        db.close()
        if sw:
            return JSONResponse(content={
                'message': 'Libro Prestado'
            })
        
        return JSONResponse(content={
                'message': 'Libro no disponible'
            })
    
    def devolverLibro(usuario_id, libro_id):
        db = Session()
        dataLibro = LibroHelper.validateLibro(db,libro_id)

        if not dataLibro:
            return JSONResponse(status_code=404, content={
                'message': 'Libro no encontrado'
            })
        
        dataUsuario = UsuarioHelper.validarUsuario(db,usuario_id)

        if not dataUsuario:
            return JSONResponse(status_code=404, content={
                'message': 'Usuario no encontrado'
            })
        
        if dataUsuario.devolver_libro(dataLibro):
            db.commit()
            db.close()
            return JSONResponse(content={
                'message': 'Libro devuelto'
            })
        
        db.close()
        return JSONResponse(content={
                'message': 'Libro no devuelto'
            })
    
    def devolverLibroByTitulo(usuario_id, titulo):
        db = Session()
        dataLibro = LibroHelper.validateLibroByTitulo(db,titulo)

        if not dataLibro:
            return JSONResponse(status_code=404, content={
                'message': 'Libro no encontrado'
            })
        
        dataUsuario = UsuarioHelper.validarUsuario(db,usuario_id)

        if not dataUsuario:
            return JSONResponse(status_code=404, content={
                'message': 'Usuario no encontrado'
            })
        
        if dataUsuario.devolver_libro(dataLibro):
            db.commit()
            db.close()
            return JSONResponse(content={
                'message': 'Libro devuelto'
            })
        
        db.close()
        return JSONResponse(content={
                'message': 'Libro no devuelto'
            })