from BD.database import Base
from sqlalchemy import Column, Integer, String, Boolean
from models.LibroBD import LibroBD
import json

class UsuarioBD(Base):
    __tablename__ = 'Usuario'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    libros_prestados = Column(String)

    def prestar_libro(self, libro: LibroBD):
        if not libro.disponible:
            lp = json.loads(self.libros_prestados)
            lp.append(libro.as_dict())
            self.libros_prestados = json.dumps(lp)
            return True
        
        return False
    
    def devolver_libro(self, libro: LibroBD):
        lp = json.loads(self.libros_prestados)
        libroDevuelto = False
        for i in range(len(lp)):
            lb = lp[i]
            if lb['id'] == libro.id:
                lp.pop(i)
                self.libros_prestados = json.dumps(lp)
                libroDevuelto = True
        if libroDevuelto:
            libro.devolver()
            return True
        
        return False