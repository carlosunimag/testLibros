from models.UsuarioBD import UsuarioBD

class UsuarioHelper:
    def validarUsuario(db,usuario_id):
        dataUsuario = db.query(UsuarioBD).filter(
            UsuarioBD.id == usuario_id
        ).first()

        if not dataUsuario:
            return False
        
        return dataUsuario