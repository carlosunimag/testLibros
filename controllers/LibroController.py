from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder 
import os
import json

from BD.database import Session
from models.LibroBD import LibroBD
from helpers.LibroHelper import LibroHelper

class LibroController:
    
    

    def createLibro(libro):
        TEST = bool(os.getenv("TEST", "False"))
        if not TEST:
            lib = LibroBD(**libro.model_dump())
            db = Session()
            db.add(lib)
            db.commit()
            db.close()
        else:
            BOOKS = []
            BOOKS.append(libro.__dict__)
            os.environ["BOOKS"] = json.dumps(BOOKS)
        
        return libro

    def getAllLibros():
        db = Session()
        data = db.query(LibroBD).all()
        db.close()
        return JSONResponse(content={
            "info":"All Books",
            "data": jsonable_encoder(data)
        }) 
    
    def getLibroById(id):
        db = Session()
        data = LibroHelper.validateLibro(db,id)
        db.close()
        if not data:
            return JSONResponse(status_code=404, content={
                'message': 'Recurso no encontrado'
            })
        
        return JSONResponse(content={
            'info':'Get Book',
            'data': jsonable_encoder(data)
        })