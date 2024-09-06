
from models.LibroBD import LibroBD

class LibroHelper:
    def validateLibro(db,libro_id):
        dataLibro = db.query(LibroBD).filter(
            LibroBD.id == libro_id
        ).first()

        if not dataLibro:
            return False
        
        return dataLibro
    
    def validateLibroByTitulo(db,titulo):
        dataLibro = db.query(LibroBD).filter(
            LibroBD.title == titulo
        ).first()

        if not dataLibro:
            return False
        
        return dataLibro
