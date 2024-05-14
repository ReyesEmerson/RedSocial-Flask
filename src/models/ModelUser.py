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
            sql = """INSERT INTO user_login (correo, password, user) VALUES (%s, %s, %s)"""
            cursor.execute(sql, (registro.correo, registro.password, registro.user))
            db.connection.commit()
            return True
        except Exception as ex:
            raise Exception(ex)
            return False    