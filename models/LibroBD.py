from BD.database import Base
from sqlalchemy import Column, Integer, String, Boolean

class LibroBD(Base):
    __tablename__ = 'libro'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    autor = Column(String)
    disponible = Column(Boolean)

    def prestar(self):
        if self.disponible :
            self.disponible = False
            return True
        
        return False
    
    def devolver(self):
        if not self.disponible :
            self.disponible = True

    def as_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'autor': self.autor,
            'disponible': self.disponible
        }