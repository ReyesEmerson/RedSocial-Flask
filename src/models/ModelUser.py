from .entities.User import User
from .entities.Registro import Registro

class ModelUser():
    
    def login(self, db, correo, password):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id, correo, password FROM user_login WHERE correo = %s"""
            cursor.execute(sql, (correo,))
            row=cursor.fetchone()
            if row is not None:
                user = User(row[0], row[1], row[2])
                if user.check_password(password):
                    return user
                else:
                    return None
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
        
    def get_user_by_email(self, db, correo):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id, correo, password FROM user_login WHERE correo = %s"""
            cursor.execute(sql, (correo,))
            row = cursor.fetchone()
            if row is not None:
                user = User(row[0], row[1], row[2])
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)    
        
class ModelRegistro():
    
    def create_registro(self, db, registro):
        try:
            cursor = db.connection.cursor()
            sql = """INSERT INTO user_login (correo, password, user, apellido, celular) VALUES (%s, %s, %s, %s, %s)"""
            cursor.execute(sql, (registro.correo, registro.password, registro.user, registro.apellido, registro.celular))
            db.connection.commit()
            return True
        except Exception as ex:
            raise Exception(ex)  
        
class ModelEditar():
    
    def actualizar(self, db, usuario_id,  correo, user, apellido, celular):
        try:
            cursor = db.connection.cursor()
            sql = """UPDATE user_login SET correo = %s, user = %s, apellido = %s, celular = %s WHERE id = %s"""
            cursor.execute(sql, (correo, user, apellido, celular, usuario_id))
            db.connection.commit()
            return True
        except Exception as ex:
            db.connection.rollback()
            raise   