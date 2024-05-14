class ModelMensaje():
    
    def enviar_mensaje(self, db, remitente_id, destinatario_id, mensaje):
        try:
            cursor = db.connection.cursor()
            sql = """INSERT INTO mensajeria (remitente_id, destinatario_id, mensaje) VALUES (%s, %s, %s)"""
            cursor.execute(sql, (remitente_id, destinatario_id, mensaje))
            db.connection.commit()
        except Exception as ex:
            db.connection.rollback()
            raise Exception(ex)
        
    def obtener_mensaje(seld, db, usuario_id):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT * FROM mensajeria WHERE remitente_id = %s OR destinatario_id = %s"""
            cursor.execute(sql, (usuario_id, usuario_id))
            mensajes = cursor.fetchall()
            return mensajes
        except Exception as ex:
            raise Exception(ex)
        
    def usuario_db(self, db):
        try:
            cursor = db.connection.cursor()
            cursor.execute("SELECT id, correo, user FROM user_login")
            usuarios = cursor.fetchall()
            return usuarios
        except Exception as e:
            print("Error al obtener usurio de la base de datos", e)
            return []