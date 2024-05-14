from werkzeug.security import check_password_hash

class User():
    
    def __init__(self, id, correo, password, user=""):
        self.id = id
        self.correo = correo
        self.password = password
        self.user = user
         
    def check_password(self, password):
        return self.password == password

    @classmethod
    def from_registro(cls, registro):
        return cls(id=None, correo=registro.correo, password=registro.password, user=registro.user)